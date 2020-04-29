import os

ADJUST_ANCHOR = {
	'rani-weekend': {
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
ANCHOR_ANIMATION = {
	'rani-weekend': {
		'direction': None,
		'offset': None,
		'speed': None,
	},
	'sophie39': {
		'direction': 'top-bottom',
		'offset': 100,
		'speed': 0.5,
	},
}
AUDIO_FMT = os.environ['AUDIO_FMT']
AUDIO_SAMPLE_RATE = 44100
BACKGROUND_PADDINGS = {
	'rani-weekend': 12,
	'sophie39': 0,
}
BUCKET_NAME = 'plasmic-stories'
CHROMA_COLOR = {
	'rani-weekend': '0x2c6937',
	'sophie39': '0x477144',
}
COMPUTE_PROJECT_NAME = 'plasmic-compute-256214'
LIBRARY_DIR_PATH = '/library'
MIN_NUM_IMAGES = 2
REQUIRED_FIELDS = ['GCSImageURLs', 'subtitle', 'text', 'title1', 'title2']
TOPIC_NAME = 'init-generate'
VIDEO_FMT = os.environ['VIDEO_FMT']
# Library assets
BACKGROUND_VIDEO_FILE_PATHS = {
	'rani-weekend': [
		'{}/backgrounds/15/30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
	'sophie39': [
		'{}/backgrounds/earth/30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
}
MASK_VIDEO_FILE_PATHS = {
	'rani-weekend': [
		'{}/masks/nanaimo-bar/mask-30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
	'sophie39': [
		'{}/masks/sophie39/mask-30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
}
MUSIC_FILE_PATHS = {
	'rani-weekend': [
		'{}/music/sr{}/1.{}'.format(LIBRARY_DIR_PATH, AUDIO_SAMPLE_RATE, AUDIO_FMT),
		'{}/music/sr{}/2.{}'.format(LIBRARY_DIR_PATH, AUDIO_SAMPLE_RATE, AUDIO_FMT),
	],
	'sophie39': [
		'{}/music/sr{}/1.{}'.format(LIBRARY_DIR_PATH, AUDIO_SAMPLE_RATE, AUDIO_FMT),
		'{}/music/sr{}/2.{}'.format(LIBRARY_DIR_PATH, AUDIO_SAMPLE_RATE, AUDIO_FMT),
	],
}
PRESENTER_BACKGROUND_VIDEO_FILE_PATHS = {
	'rani-weekend': [
		'{}/presenter-bgs/855brannan/25fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
		'{}/presenter-bgs/oakland/25fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
	'sophie39': [
		'{}/presenter-bgs/sun-2/30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
		'{}/presenter-bgs/sun-2/30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
		'{}/presenter-bgs/sun-2/30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
		'{}/presenter-bgs/space-travel/30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
}
TRANSITION_FILE_PATHS = {
	'rani-weekend': [
		'{}/transitions/2/mid.yaml'.format(LIBRARY_DIR_PATH),
	],
	'sophie39': [
		'{}/transitions/3/mid.yaml'.format(LIBRARY_DIR_PATH),
	],
}
TRANSITION_VIDEO_FILE_PATHS = {
	'rani-weekend': [
		'{}/transitions/2/30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
	'sophie39': [
		'{}/transitions/3/30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
	],
}
