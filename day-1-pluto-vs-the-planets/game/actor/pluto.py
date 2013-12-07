# ----------- Pluto ----------
# 
# -----------------------------


# -------- Imports --------
import pygame, math, app.config as config

from app.actor import Actor
from app.player import Player
from app.sprite import StaticSprite, AnimatedSprite
from app.vector import Vector

config.spriteGroups['player'] = pygame.sprite.Group( )
config.spriteGroups['player_bullet'] = pygame.sprite.Group( )

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

		self.sprite.add( config.spriteGroups['player'] )

		# Controls
		self.addControlDown( pygame.K_LEFT,  self.moveLeft )
		self.addControlDown( pygame.K_RIGHT, self.moveRight )
		self.addControlDown( pygame.K_UP,    self.moveUp )
		self.addControlDown( pygame.K_DOWN,  self.moveDown )

		self.addControlUp( pygame.K_LEFT,  self.stopLeft )
		self.addControlUp( pygame.K_RIGHT, self.stopRight )
		self.addControlUp( pygame.K_UP,    self.stopUp )
		self.addControlUp( pygame.K_DOWN,  self.stopDown )

		self.addControlDown( pygame.K_z, self.shootGuns )
		self.addControlUp( pygame.K_z, self.stopShootingGuns )

		# Set default speed
		self.speed = 7

		self.isFiringGuns = False
		self.gunFireRate = 5
		self.gunCoolDown = 0
		self.gunBulletSpeed = 40

		self.isFiringBeam = False

	def shootGuns( self ):
		self.isFiringGuns = True

	def stopShootingGuns( self ):
		self.isFiringGuns = False

	def update( self, frameTime, lifeTime ):
		Player.update( self, frameTime, lifeTime )

		if self.isFiringGuns and self.gunCoolDown == 0:
			self.gunCoolDown = self.gunFireRate

			y = self.sprite.rect.y + ( self.sprite.rect.height / 2 )

			Bullet(
				Vector( self.sprite.rect.centerx - 16, y ),
				Vector( -12, -self.gunBulletSpeed )
			)
			Bullet(
				Vector( self.sprite.rect.centerx - 8, y ),
				Vector( -6, -self.gunBulletSpeed )
			)
			Bullet(
				Vector( self.sprite.rect.centerx, y ),
				Vector( 0, -self.gunBulletSpeed )
			)
			Bullet(
				Vector( self.sprite.rect.centerx + 8, y ),
				Vector( 6, -self.gunBulletSpeed )
			)
			Bullet(
				Vector( self.sprite.rect.centerx + 16, y ),
				Vector( 12, -self.gunBulletSpeed )
			)

		elif self.gunCoolDown > 0:
			self.gunCoolDown -= 1


class Bullet( Actor ):
	def __init__( self, vector=Vector(0,0), moveVector=Vector(0,-1) ):
		Actor.__init__( self )

		self.sprite = StaticSprite( 'player/bullet.png', vector )

		self.sprite.add( config.spriteGroups['player_bullet'] )

		self.vector = vector.subtract( Vector(
			self.sprite.rect.width / 2,
			self.sprite.rect.height
		))
		self.moveVector = moveVector

		self.sprite.image = pygame.transform.rotate(
			self.sprite.image, 
			90 - math.atan2( self.moveVector.y, self.moveVector.x ) * 180 / math.pi
		)

	def update( self, frameTime, lifeTime ):
		self.vector.add( self.moveVector )

		if self.vector.y < 0 - self.sprite.rect.height:
			self.sprite.kill()