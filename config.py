import os

ADJUST_ANCHOR = {
	'nanaimo-bar': {
		'rotate': 0,
		'scaleWidth': 0,
		'scaleHeight': 0,
		'x': 0,
		'y': 0,
	},
	'sophie39': {
		'rotate': 12,
		'scaleWidth': 142,
		'scaleHeight': 283,
		'x': 220,
		'y': 410,
	},
}
AUDIO_FMT = os.environ['AUDIO_FMT']
AUDIO_SAMPLE_RATE = 44100
BUCKET_NAME = 'plasmic-stories'
COMPUTE_PROJECT_NAME = 'plasmic-compute-256214'
LIBRARY_DIR_PATH = '/library'
MIN_NUM_IMAGES = 2
REQUIRED_FIELDS = ['GCSImageURLs', 'subtitle', 'text', 'title1', 'title2']
TOPIC_NAME = 'init-generate'
VIDEO_FMT = os.environ['VIDEO_FMT']
# Library assets
BACKGROUND_VIDEO_FILE_PATHS = {
	'nanaimo-bar': [
		'{}/backgrounds/15/30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
	'sophie39': [
		'{}/backgrounds/15/30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
}
MASK_VIDEO_FILE_PATHS = {
	'nanaimo-bar': [
		'{}/masks/nanaimo-bar/mask-30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
	'sophie39': [
		'{}/masks/sophie39/mask-30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
}
MUSIC_FILE_PATHS = {
	'nanaimo-bar': [
		'{}/music/sr{}/1.{}'.format(LIBRARY_DIR_PATH, AUDIO_SAMPLE_RATE, AUDIO_FMT),
		'{}/music/sr{}/2.{}'.format(LIBRARY_DIR_PATH, AUDIO_SAMPLE_RATE, AUDIO_FMT),
	],
	'sophie39': [
		'{}/music/sr{}/1.{}'.format(LIBRARY_DIR_PATH, AUDIO_SAMPLE_RATE, AUDIO_FMT),
		'{}/music/sr{}/2.{}'.format(LIBRARY_DIR_PATH, AUDIO_SAMPLE_RATE, AUDIO_FMT),
	],
}
PRESENTER_BACKGROUND_VIDEO_FILE_PATHS = {
	'nanaimo-bar': [
		'{}/presenter-bgs/855brannan/25fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
		'{}/presenter-bgs/oakland/25fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
	'sophie39': [
		'{}/presenter-bgs/sun/30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
}
TRANSITION_FILE_PATHS = {
	'nanaimo-bar': [
		'{}/transitions/120/mid.yaml'.format(LIBRARY_DIR_PATH),
	],
	'sophie39': [
		'{}/transitions/2/mid.yaml'.format(LIBRARY_DIR_PATH),
	],
}
TRANSITION_VIDEO_FILE_PATHS = {
	'nanaimo-bar': [
		'{}/transitions/120/30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
	'sophie39': [
		'{}/transitions/120/30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
}
