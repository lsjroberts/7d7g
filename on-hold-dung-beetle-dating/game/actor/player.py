# ----------- Beetle ----------
# 
# -----------------------------


# -------- Imports --------
import pygame, math, app.config as config

from app.player import Player
from app.sprite import AnimatedSprite
from app.vector import Vector

config.spriteGroups['player'] = pygame.sprite.Group( )

# ----------- Player -----------
#
class Beetle( Player ):
	def __init__( self, vector=Vector(0,0) ):
		Player.__init__( self )

		self.vector = vector

		# Sprite
		sprite = AnimatedSprite( 'player/beetle.png', vector )
		sprite.addAnimationState( 'idle-right', 0, 0, 100 )
		sprite.addAnimationState( 'walking-right', 1, 5, 10 )
		sprite.setAnimationState( 'idle-right' )
		self.setSprite( sprite )

		self.sprite.add( config.spriteGroups['player'] )