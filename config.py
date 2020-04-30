import os

ADJUST_ANCHOR = {
	'rani-weekend': {
		'rotate': 0,
		'scaleHeight': 471,
		'scaleWidth': 238,
		'x': 135,
		'y': 274,
	},
	'sophie39': {
		'rotate': 12,
		'scaleHeight': 283,
		'scaleWidth': 142,
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
CHROMA = {
	'rani-weekend': {
		'color': 'green',
		'overlay': 0.1,
		'sensitivity': 0.3,
	},
	'sophie39': {
		'color': '0x477144',
		'overlay': 0,
		'sensitivity': 0.1,
	},
}
COMPUTE_PROJECT_NAME = 'plasmic-compute-256214'
LANDMARKS = {
	'rani-weekend': {
		'minPercentage': 0.5,
		'percentageClip': 1.2,
	},
	'sophie39': {
		'minPercentage': 0.5,
		'percentageClip': 2,
	},
}
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
		'{}/masks/rani-weekend/mask-30fps-512x1024.{}'.format(LIBRARY_DIR_PATH, VIDEO_FMT),
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
