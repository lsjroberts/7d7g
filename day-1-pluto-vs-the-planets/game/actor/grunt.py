# ------------------- Grunts --------------------
# Generic shitty bad guys who die by the hundreds
# -----------------------------------------------


# -------- Imports --------
import pygame, math, app.config as config

from app.app import UpdateableGameObject
from app.actor import AIActor, KillableActor
from app.collision import Collider
from app.event import EventListener
from app.sprite import AnimatedSprite
from app.vector import Vector

from game.sprite.explosions import Explosion

config.spriteGroups['grunt'] = pygame.sprite.Group( )
config.spriteGroups['grunt_bullet'] = pygame.sprite.Group( )

def gruntHitByBullet( sprite ):
	sprite.actor.takeDamage( 1 )

c = Collider(
	config.spriteGroups['grunt'],
	config.spriteGroups['player_bullet'],
	gruntHitByBullet
)
# c.killB = True
config.app.addCollider( c )

# -------- Grunt --------
#
class Grunt( AIActor, KillableActor ):
	def __init__( self, vector=Vector(0,0) ):
		AIActor.__init__( self )
		self.vector = vector

		# Sprite
		sprite = AnimatedSprite( 'mars/grunt.png', vector )
		sprite.addAnimationState( 'idle', 0, 0, 100 )
		sprite.setAnimationState( 'idle' )
		self.setSprite( sprite )

		sprite.add( config.spriteGroups['grunt'] )

		self.setHealth( 1 )

		self.fireChance = .1
	
	def die( self ):
		Explosion( Vector(self.sprite.rect.centerx, self.sprite.rect.centery) )
		KillableActor.die( self )

	def update( self, frameTime, lifeTime ):
		AIActor.update( self, frameTime, lifeTime )


class Formation( UpdateableGameObject ):
	def __init__( self, numGrunts, vector, movePattern ):
		UpdateableGameObject.__init__( self )

		self.numGrunts = numGrunts
		self.vector = vector
		self.movePattern = movePattern
		self.grunts = []

		for n in range( 0, numGrunts ):
			self.grunts.append( Grunt(Vector(vector.x, vector.y)) )

	def update( self, frameTime, lifeTime ):
		for grunt in self.grunts:
			self.movePattern.move( grunt )


class SquareFormation( Formation ):
	def __init__( self, numGrunts, vector, movePattern=None ):
		if movePattern is None: movePattern = DirectionMovePattern( Vector(0,2) )
		Formation.__init__( self, numGrunts, vector, movePattern )

		# Take the square root of the number of grunts to get the length of
		# each side.
		sideLength = math.ceil( math.sqrt(self.numGrunts) )

		spacingX = self.grunts[0].sprite.rect.width * 1.5
		spacingY = self.grunts[0].sprite.rect.height * 1.2

		x = 1
		y = 1
		for grunt in self.grunts:
			if x > sideLength:
				x = 1
				y += 1
			grunt.vector.add( Vector(
				spacingX * (x - 1),
				spacingY * (y - 1)
			))

			x += 1

class DiamondFormation( Formation ):
	def __init__( self, numGrunts, vector, movePattern=None ):
		if movePattern is None: movePattern = DirectionMovePattern( Vector(0,2) )
		Formation.__init__( self, numGrunts, vector, movePattern )

		# Take the square root of the number of grunts to get the length of
		# each side.
		sideLength = math.ceil( math.sqrt(self.numGrunts) )

		spacingX = self.grunts[0].sprite.rect.width * 1
		spacingY = self.grunts[0].sprite.rect.height * 1

		x = 1
		y = sideLength
		i = 0
		j = 0
		for grunt in self.grunts:
			if j == sideLength:
				i += 1
				y = sideLength + i
				x = i + 1
				j = 0

			grunt.vector.add( Vector(
				spacingX * (x - 1),
				spacingY * (y - 1)
			))

			j += 1
			x += 1
			y -= 1


class CircleFormation( Formation ):
	pass


class SpiralFormation( Formation ):
	pass


class MovePattern( ):
	pass


class DirectionMovePattern( MovePattern ):
	def __init__( self, vector=Vector(0,1) ):
		self.vector = vector

	def move( self, grunt ):
		grunt.vector.add( self.vector )


class GruntHitListener( EventListener ):
	pass

# config.event.registerListener( GruntHitListener() )