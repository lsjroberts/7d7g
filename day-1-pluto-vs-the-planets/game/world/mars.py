# ---------- Level - Mars ----------
#
# ----------------------------------


# -------- Imports --------

from app.world import World
from game.scene.mars.space import Space
# from game.scene.mars.surface import MarsSurfaceScene
from game.actor.pluto import Pluto


# ----------- Mars -----------
#
class Mars( World ):

	def __init__( self ):
		World.__init__( self )
		self.setScene( Space() )
		self.scene.addActor( Pluto() )