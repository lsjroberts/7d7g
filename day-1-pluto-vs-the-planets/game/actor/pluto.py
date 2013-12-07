# ----------- Pluto ----------
# 
# -----------------------------


# -------- Imports --------
import pygame

from app.player import Player
from app.sprite import AnimatedSprite
from app.vector import Vector


# ----------- Pluto -----------
#
class Pluto( Player ):
	def __init__( self, vector=Vector(0,0) ):
		Player.__init__( self )

		# Sprite
		sprite = AnimatedSprite( 'player/pluto.png', vector )
		sprite.addAnimationState( 'idle', 0, 0, 100 )
		sprite.setAnimationState( 'idle' )
		self.setSprite( sprite )

		# Controls
		self.addControlDown(pygame.K_LEFT,  self.moveLeft)
		self.addControlDown(pygame.K_RIGHT, self.moveRight)
		self.addControlDown(pygame.K_UP,    self.moveUp)
		self.addControlDown(pygame.K_DOWN,  self.moveDown)

		self.addControlUp(pygame.K_LEFT,  self.stopLeft)
		self.addControlUp(pygame.K_RIGHT, self.stopRight)
		self.addControlUp(pygame.K_UP,    self.stopUp)
		self.addControlUp(pygame.K_DOWN,  self.stopDown)

		# Set default speed
		self.speed = 6