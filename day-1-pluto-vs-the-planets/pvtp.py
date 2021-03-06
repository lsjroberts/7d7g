# ------------ Pluto vs The Planets ------------
# Day 1 of "7 days 7 games"
# @author Laurence Roberts
# ----------------------------------------------


# -------- Init --------

# Import config
import app.config as config
config.settings['title'] = "Pluto vs The Planets - 7d7g"
config.settings['screen_w'] = 1200
config.settings['screen_h'] = 900
config.settings['game_w'] = 1600

# Initialise pygame
import pygame

# if 'windows' == config.settings['platform']:
# 	import pygame._view

pygame.init( )

# Create the app
from app.app import App
from app.event import PygameEvent
app = config.app = App( )

# Setup the screen
config.screen = pygame.display.set_mode( [
	config.settings['screen_w'],
	config.settings['screen_h']
] )
pygame.display.set_caption( config.settings['title'] )
# pygame.display.set_icon(pygame.image.load('sprites/player/player-life.png').convert_alpha())
config.screen.convert( )

# Create the clock
clock = pygame.time.Clock( )



# -------- TEMPORARY --------
config.sprites = pygame.sprite.LayeredUpdates( )
config.spriteGroups['all'] = pygame.sprite.Group( )

from app.vector import Vector
config.game_offset = Vector(0, 0)
config.frame_offset = Vector(2, 0)
config.player_vector = Vector(0, 0)

from game.world.mars import Mars
app.setMode( 'game' )
app.setWorld( Mars() )
# ------ ENDTEMPORARY -------



# -------- Game Loop --------
while app.running:

	# Capture events
	for e in pygame.event.get( ):
		event = PygameEvent( e )
		app.events.post( event )

	# Process tick
	clock.tick( config.settings['fps'] )
	app.tick( clock.get_time(), pygame.time.get_ticks() )


# -------- Exit --------
pygame.quit( )