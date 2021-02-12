import os
import yaml

from apache_beam.io.gcp import gcsio
from config import *
from flask import Flask, request
from google.cloud import pubsub_v1, storage
from random import choice


app = Flask(__name__)

client = storage.Client()
dest_bucket = client.get_bucket(STORIES_BUCKET_NAME)
library_bucket = client.get_bucket(LIBRARY_BUCKET_NAME)

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(COMPUTE_PROJECT_NAME, TOPIC_NAME)


@app.route('/stories/<story_id>', methods=['POST'])
def add_story(story_id):
	data = request.get_json()
	# Validate data
	if not all(elem in data for elem in REQUIRED_FIELDS) \
		or len(data['GCSImageURLs']) < MIN_NUM_IMAGES:
		print('raise:', data)
		raise
	# Copy images to plasmic bucket
	img_filenames = []
	for gcs_url in data['GCSImageURLs']:
		source_bucket_name, source_filepath = gcsio.parse_gcs_path(gcs_url)
		source_bucket = client.get_bucket(source_bucket_name)
		source_blob = source_bucket.get_blob(source_filepath)

		img_filename = source_filepath.split('/')[-1]
		img_filenames.append(img_filename)
		dest_filepath = '{}/{}'.format(story_id, img_filename)
		source_bucket.copy_blob(source_blob, dest_bucket, dest_filepath)
	# Create story yaml file
	model = data['model']
	template = load_template(model)
	data = {
		'adjustAnchor': template['adjustAnchor'],
		'anchorAnimation': template['anchorAnimation'],
		'bgPadding': template['backgroundPadding'],
		'category': data['category'].strip(),
		'chroma': template['chroma'], 
		'images': img_filenames,
		'landmarks': template['landmarks'],
		'library': {
			'bgVideoFilePath': choice(template['backgroundVideoFilePaths']),
			'maskVideoFilePath': choice(template['maskVideoFilePaths']),
			'musicFilePath': choice(template['musicFilePaths']),
			'presenterBgVideoFilePath': choice(template['presenterBackgroundVideoFilePaths']),
			'transitionFilePath': choice(template['transitionFilePaths']),
			'transitionVideoFilePath': choice(template['transitionVideoFilePaths']),
		},
		'model': model,
		'showAnchor': data['showAnchor'],
		'subtitle': data['subtitle'],
		'text': data['text'],
		'title': [
			data['title1'],
			data['title2'],
			data['title3']
		],
	}
	story_filepath = '/tmp/{}.yaml'.format(story_id)
	with open(story_filepath, 'w') as f:
		yaml.dump(data, f, default_flow_style=False)
	# Upload yaml to story bucket
	dest_filepath = '{}/story.yaml'.format(story_id)
	blob = dest_bucket.blob(dest_filepath)
	blob.upload_from_filename(story_filepath)
	os.remove(story_filepath)
	# Create pubsub message
	data = story_id.encode('utf-8') # data must be a bytestring
	publisher.publish(topic_path, data=data)

	return 'ok'

def load_template(name):
	path = 'templates/{}.yaml'.format(name)
	blob = library_bucket.get_blob(path)
	data = blob.download_as_string()
	return yaml.load(data, Loader=yaml.FullLoader)
