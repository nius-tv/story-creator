import yaml

from apache_beam.io.gcp import gcsio
from config import *
from flask import Flask, request
from google.cloud import pubsub_v1, storage


app = Flask(__name__)

client = storage.Client()
dest_bucket = client.get_bucket(BUCKET_NAME)

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(COMPUTE_PROJECT_NAME, TOPIC_NAME)


@app.route('/stories/<story_id>', methods=['POST'])
def add_story(story_id):
	data = request.get_json()
	# Validates data
	if not all(elem in data for elem in REQUIRED_FIELDS) \
		or len(data['GCSURLs']) < MIN_NUM_IMAGES:
		print('raise:', data)
		raise
	# Copy images to plasmic bucket
	img_filenames = []
	for gcs_url in data['GCSURLs']:
		source_bucket_name, source_filepath = gcsio.parse_gcs_path(gcs_url)
		source_bucket = client.get_bucket(source_bucket_name)
		source_blob = source_bucket.get_blob(source_filepath)

		img_filename = source_filepath.split('/')[-1]
		img_filenames.append(img_filename)
		dest_filepath = '{}/{}'.format(story_id, img_filename)
		source_bucket.copy_blob(source_blob, dest_bucket, dest_filepath)
	# Create story yaml file
	story_filepath = '/tmp/{}.yaml'.format(story_id)
	data = {
		'category': data['category'].strip(),
		'images': img_filenames,
		'pixToPixModel': PIX_TO_PIX_MODEL,
		'subtitle': clean_text(data['subtitle']),
		'text': clean_text(data['text']),
		'title': [
			clean_text(data['title1']),
			clean_text(data['title2'])
		]
	}
	with open(story_filepath, 'w') as f:
		yaml.dump(data, f, default_flow_style=False)
	# Upload yaml to story bucket
	dest_filepath = '{}/story.yaml'.format(story_id)
	blob = dest_bucket.blob(dest_filepath)
	blob.upload_from_filename(story_filepath)
	# Create pubsub message
	data = story_id.encode('utf-8') # data must be a bytestring
	publisher.publish(topic_path, data=data)

	return 'ok'


def clean_text(text):
	return text\
		.replace('\n', ' ')\
		.replace('\u2019', '\'')\
		.replace('  ', ' ')\
		.strip()
