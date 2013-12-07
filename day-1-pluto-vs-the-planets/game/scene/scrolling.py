# ---------- Scrolling Scene -----------
# Scenes that can scroll vertically or
# horizontally.
# --------------------------------------

# -------- Imports --------

from app.app import UpdateableGameObject
from app.scene import Scene
from app.vector import Vector


# ----------- Vertical Scrolling Scene -----------
# A scene automatically scrolls vertically at a
# set speed.
class VerticalScrollingScene( Scene, UpdateableGameObject ):
	def __init__( self, verticalSpeed=0 ):
		Scene.__init__( self )
		UpdateableGameObject.__init__( self )

		self.verticalSpeed = verticalSpeed

	def update( self, frameTime, lifeTime ):
		for layer in self.layers:
			if layer.vector.y < 0:
				layer.vector.add( Vector(0, self.verticalSpeed) )
			else:
				layer.vector.y = 0