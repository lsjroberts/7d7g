# ------------------- Grunts --------------------
# Generic shitty bad guys who die by the hundreds
# -----------------------------------------------


# -------- Imports --------
import pygame, math, random, app.config as config

from app.app import UpdateableGameObject
from app.actor import Actor, AIActor, KillableActor
from app.collision import Collider
from app.event import EventListener
from app.sprite import AnimatedSprite, StaticSprite
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
c.killB = True
config.app.addCollider( c )

# -------- Grunt --------
#
class Grunt( AIActor, KillableActor ):
	def __init__( self, vector=Vector(0,0) ):
		AIActor.__init__( self )
		self.vector = vector

		# Sprite
		sprite = AnimatedSprite( 'mars/grunt.png', vector )
		sprite.addAnimationState( 'idle', 0, 3, 4 )
		sprite.addAnimationState( 'damaged', 4, 4, 100 )
		sprite.setAnimationState( 'idle' )
		self.setSprite( sprite )

		sprite.add( config.spriteGroups['grunt'] )

		self.setHealth( 3 )
		self.damagedTimer = 0

		self.formation = None

	def takeDamage( self, damage ):
		KillableActor.takeDamage( self, damage )
		self.sprite.setAnimationState( 'damaged' )
		self.damagedTimer = 5
	
	def die( self ):
		Explosion( Vector(self.sprite.rect.centerx, self.sprite.rect.centery) )
		KillableActor.die( self )
		self.formation.grunts.remove( self )

	def update( self, frameTime, lifeTime ):
		self.vector.add( config.frame_offset )
		AIActor.update( self, frameTime, lifeTime )

		if self.vector.y > config.settings['screen_h'] * 2:
			self.kill( )

		if self.sprite.state == 'damaged' and self.damagedTimer > 0:
			self.damagedTimer -= 1
			if self.damagedTimer == 0:
				self.sprite.setAnimationState( 'idle' )


class Formation( UpdateableGameObject ):
	def __init__( self, numGrunts, vector, movePattern ):
		UpdateableGameObject.__init__( self )

		self.numGrunts = numGrunts
		self.vector = vector
		self.movePattern = movePattern
		self.grunts = []

		self.fireChance = .5

		for n in range( 0, numGrunts ):
			g = Grunt(Vector(vector.x, vector.y))
			g.formation = self
			self.grunts.append( g )

	def update( self, frameTime, lifeTime ):
		self.vector.add( self.movePattern.vector )
		self.vector.add( config.frame_offset )

		for grunt in self.grunts:
			self.movePattern.move( grunt )

		r = random.randint(0, 10000) / 100.0
		if r <= self.fireChance:
			for grunt in self.grunts:
				Bullet( grunt.vector.copy(), config.player_vector.copy().subtract(self.vector.copy().subtract(grunt.vector)) )


class SquareFormation( Formation ):
	def __init__( self, numGrunts, vector, movePattern=None ):
		if movePattern is None: movePattern = DirectionMovePattern( Vector(0,2) )
		Formation.__init__( self, numGrunts, vector, movePattern )

		# Take the square root of the number of grunts to get the length of
		# each side.
		sideLength = math.ceil( math.sqrt(self.numGrunts) )

		spacingX = self.grunts[0].sprite.rect.width * 1.5
		spacingY = self.grunts[0].sprite.rect.height * 1.2

		offsetX = (spacingX * sideLength) / 2.0
		offsetY = (spacingX * sideLength) / 2.0

		x = 1
		y = 1
		for grunt in self.grunts:
			if x > sideLength:
				x = 1
				y += 1
			grunt.vector.add( Vector(
				spacingX * (x - 1) - offsetX,
				spacingY * (y - 1) - offsetY
			))

			x += 1

class DiamondFormation( Formation ):
	def __init__( self, numGrunts, vector, movePattern=None ):
		if movePattern is None: movePattern = DirectionMovePattern( Vector(0,2) )
		Formation.__init__( self, numGrunts, vector, movePattern )

		# Take the square root of the number of grunts to get the length of
		# each side.
		sideLength = math.ceil( math.sqrt(self.numGrunts) )

		spacingX = self.grunts[0].sprite.rect.width * 1.0
		spacingY = self.grunts[0].sprite.rect.height * 1.0

		offsetX = (spacingX * sideLength) / 2.0
		offsetY = (spacingX * sideLength) / 2.0

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
				spacingX * (x - 1) - offsetX,
				spacingY * (y - 1) - offsetY
			))

			j += 1
			x += 1
			y -= 1


class CircleFormation( Formation ):
	pass


# ----------- Spiral Formation -----------
# http://stackoverflow.com/questions/13894715/draw-equidistant-points-on-a-spiral
class SpiralFormation( Formation ):
	def __init__( self, numGrunts, vector, movePattern=None ):
		if movePattern is None: movePattern = DirectionMovePattern( Vector(0,2) )
		Formation.__init__( self, numGrunts, vector, movePattern )

		self.rotation = 0.0
		self.repositionGrunts( )

	def repositionGrunts( self ):
		radius = len(self.grunts) * 50
		coils = len(self.grunts) * 2

		# value of theta corresponding to end of last coil
		thetaMax = coils * 2 * math.pi

		awayStep = radius / thetaMax
		spacing = self.grunts[0].sprite.rect.width / 2

		i = 0
		theta = spacing / awayStep
		while theta <= thetaMax:
			away = awayStep * theta
			around = theta + (self.rotation / 360)
			x = self.vector.x + (math.cos( around ) * math.pi) * away
			y = self.vector.y + (math.sin( around ) * math.pi) * away

			try:
				self.grunts[i].vector.x = x
				self.grunts[i].vector.y = y
			except IndexError:
				break

			theta += spacing / away
			i += 1

	def update( self, frameTime, lifeTime ):
		if len(self.grunts) <= 0:
			self.removeGameObject( )
			return

		Formation.update( self, frameTime, lifeTime )
		self.rotation += (frameTime / 1000) + 9.0
		self.repositionGrunts( )


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



class Bullet( Actor ):
	def __init__( self, vector=Vector(0,0), targetVector=Vector(0,-1) ):
		Actor.__init__( self )

		self.sprite = StaticSprite( 'mars/bullet.png', vector )

		self.sprite.add( config.spriteGroups['grunt_bullet'] )

		self.vector = vector.subtract( Vector(
			self.sprite.rect.width / 2,
			self.sprite.rect.height
		))

		self.moveVector = Vector(5, 5).dot( self.vector.copy().subtract( targetVector ).unit() )

	def update( self, frameTime, lifeTime ):
		self.vector.add( self.moveVector )
		self.vector.add( config.frame_offset )
		Actor.update( self, frameTime, lifeTime )

		if self.vector.y > config.settings['screen_h'] or self.vector.y < 0 or self.vector.x < 0 or self.vector.x > config.settings['screen_w']:
			self.kill()