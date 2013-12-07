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
		sprite.addAnimationState( 'idle', 0, 3, 2 )
		sprite.setAnimationState( 'idle' )
		self.setSprite( sprite )

		# Controls
		self.addControlHold(pygame.K_LEFT, self.moveLeft)
		self.addControlHold(pygame.K_RIGHT, self.moveRight)
		self.addControlHold(pygame.K_UP, self.moveUp)
		self.addControlHold(pygame.K_DOWN, self.moveDown)

		self.moveVector = Vector( 0, 0 )

	def moveLeft( self ):
		self.move( self.moveVector.add(
			Vector( -self.speed, self.moveVector.y )
		))

	def moveRight( self ):
		self.move( self.moveVector.add(
			Vector( self.speed, self.moveVector.y )
		))

	def moveUp( self ):
		self.move( self.moveVector.add(
			Vector( self.moveVector.x, -self.speed )
		))

	def moveDown( self ):
		self.move( self.moveVector.add(
			Vector( self.moveVector.x, self.speed )
		))