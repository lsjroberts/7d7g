# ---------- Scene - Mars -----------
# 
# -----------------------------------

# -------- Imports --------

import app.config as config
from app.scene import Scene, SceneLayer


# ----------- Mars Scene -----------
# 
class Space( Scene ):

	def __init__( self ):
		Scene.__init__( self )

		self.addLayer( SceneLayer(
			'mars/space.jpg',
			config.spriteLayers['sceneFar']
		) )