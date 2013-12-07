# ----------- Explosions -----------
# BOOM!
# ----------------------------------


# -------- Imports --------
from app.sprite import PlayOnceAnimatedSprite


# ----------- Explosion -----------
# Boom
class Explosion( PlayOnceAnimatedSprite ):
	def __init__( self, vector ):
		PlayOnceAnimatedSprite.__init__( self, 'effects/explosion.png', vector )
		self.addAnimationState( 'explode', 0, 7, 8 )
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