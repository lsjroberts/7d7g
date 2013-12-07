# ----------- Pluto ----------
# 
# -----------------------------


# -------- Imports --------

from app.player import Player
from app.sprite import AnimatedSprite
from app.vector import Vector


# ----------- Pluto -----------
#
class Pluto( Player ):

	def __init__( self, vector=Vector(0,0) ):
		sprite = AnimatedSprite( 'player/pluto.png', vector )

		sprite.addAnimationState( 'idle', 0, 3, 2 )

		sprite.setAnimationState( 'idle' )

		self.setSprite( sprite )