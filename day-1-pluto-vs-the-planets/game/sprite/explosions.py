# ----------- Explosions -----------
# BOOM!
# ----------------------------------


# -------- Imports --------
from app.sprite import PlayOnceAnimatedSprite
from app.vector import Vector


# ----------- Explosion -----------
# Boom
class Explosion( PlayOnceAnimatedSprite ):
	def __init__( self, vector ):
		vector.subtract( Vector(32,32))

		PlayOnceAnimatedSprite.__init__( self, 'effects/explosion.png', vector )
		self.addAnimationState( 'explode', 0, 7, 6 )
		self.setAnimationState( 'explode' )


# ----------- Small Explosion -----------
# boom
class SmallExplosion( PlayOnceAnimatedSprite ):
	def __init__( self, vector ):
		PlayOnceAnimatedSprite.__init__( 'effects/small-explosion.png', vector )


# ----------- Large Explosion -----------
# BOOOOOOM!
class LargeExplosion( PlayOnceAnimatedSprite ):
	def __init__( self, vector ):
		PlayOnceAnimatedSprite.__init__( 'effects/large-explosion.png', vector )