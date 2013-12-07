# ------------------- Grunts --------------------
# Generic shitty bad guys who die by the hundreds
# -----------------------------------------------


# -------- Imports --------
import math
from app.app import UpdateableGameObject
from app.actor import AIActor
from app.sprite import AnimatedSprite
from app.vector import Vector


# -------- Grunt --------
#
class Grunt( AIActor ):
	def __init__( self, vector=Vector(0,0) ):
		AIActor.__init__( self )
		self.vector = vector

		# Sprite
		sprite = AnimatedSprite( 'mars/grunt.png', vector )
		sprite.addAnimationState( 'idle', 0, 0, 100 )
		sprite.setAnimationState( 'idle' )
		self.setSprite( sprite )
	
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
	def __init__( self, numGrunts, vector ):
		Formation.__init__( self, numGrunts, vector, MoveDownPattern(2) )

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
	pass


class CircleFormation( Formation ):
	pass


class SpiralFormation( Formation ):
	pass


class MovePattern( ):
	pass


class MoveDownPattern( MovePattern ):
	def __init__( self, speed=1 ):
		self.speed = speed

	def move( self, grunt ):
		grunt.vector.y += self.speed