# ---------- Level - Dirt ----------
#
# ----------------------------------


# -------- Imports --------

from app.world import World
from game.scene.dirt import Dirt as DirtScene


# ----------- Dirt -----------
#
class Dirt( World ):

	def __init__( self ):
		World.__init__( self )
		self.setScene( DirtScene() )