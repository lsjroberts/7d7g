# ---------- Scrolling Scene -----------
# Scenes that can scroll vertically or
# horizontally.
# --------------------------------------

# -------- Imports --------
import app.config as config

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


class HorizontalScrollingScene( Scene, UpdateableGameObject ):
	def update( self, frameTime, lifeTime ):
		sw = config.settings['screen_w'] * 1.0
		gw = config.settings['game_w'] * 1.0
		px = config.player_vector.x * 1.0

		before = config.game_offset.copy()
		config.game_offset  = Vector( 0.0 - ((px / sw) * (gw - sw)), 0 )
		config.frame_offset = config.game_offset.copy().subtract( before )

		for layer in self.layers:
			layer.vector.x = config.game_offset.x