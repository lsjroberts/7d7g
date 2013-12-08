# ---------- Scene - Dirt -----------
# 
# -----------------------------------

# -------- Imports --------

import app.config as config
from app.scene import Scene, SceneLayer
from app.vector import Vector
from game.actor.player import Beetle

# ----------- Dirt Scene -----------
# 
class Dirt( Scene ):

	def __init__( self ):
		Scene.__init__( self )

		bg = SceneLayer(
			'dirt/dirt.png',
			config.spriteLayers['sceneFar']
		)
		bg.vector.y = config.settings['screen_h'] - bg.rect.height
		bg.vector.x = 0
		self.addLayer( bg )

		beetle = Beetle( Vector(
			0,
			config.settings['screen_h']
		))
		self.addActor( beetle )