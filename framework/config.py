# ----------- Config ----------
# Shared configuration across all modules
# -----------------------------

from sys import platform

settings = {
	'title': 'TCP',
	'fps': 60,
	'platform': 'unknown',
	'screen_w': 800,
	'screen_h': 600,
	'screen_fill': (20,169,123)
}

if 'linux' == platform or 'linux2' == platform:
	settings['platform'] = 'linux'
elif 'darwin' == platform:
	settings['platform'] = 'mac'
elif 'win32' == platform or 'cygwin' == platform:
	settings['platform'] = 'windows'


folders = {
	'assets': 'assets/',
	'sprites': 'assets/sprites/',
	'scenes': 'assets/scenes/',
	'data': 'data/',
	'story': 'data/story/'
}


sprites = None

spriteLayers = {
	'conversation': 100,
	'sceneNear': 200,
	'player': 300,
	'actor': 400,
	'sceneFar': 500
}

spriteGroups = {

}


world = {

}


colours = {

}


app = None
screen = None