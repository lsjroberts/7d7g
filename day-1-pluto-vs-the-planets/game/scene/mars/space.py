# ---------- Scene - Mars -----------
# 
# -----------------------------------

# -------- Imports --------

import app.config as config
from app.scene import SceneLayer
from app.vector import Vector
from game.scene.scrolling import VerticalScrollingScene
from game.actor.pluto import Pluto
from game.actor.grunt import SquareFormation
from game.actor.grunt import DirectionMovePattern

# ----------- Mars Scene -----------
# 
class Space( VerticalScrollingScene ):

	def __init__( self ):
		VerticalScrollingScene.__init__( self, .5 )

		bg = SceneLayer(
			'mars/space.gif',
			config.spriteLayers['sceneFar']
		)
		bg.vector.y = config.settings['screen_h'] - bg.rect.height
		bg.vector.x = 0 - (config.settings['screen_w'] / 4)
		self.addLayer( bg )

		pluto = Pluto()
		pluto.vector.x = (config.settings['screen_w'] / 2) - (pluto.sprite.rect.width / 2)
		pluto.vector.y = config.settings['screen_h'] - (pluto.sprite.rect.height * 1.5)
		self.addActor( pluto )

		formation = SquareFormation( 9, Vector(100,100), DirectionMovePattern(Vector(2,4)) )
		for grunt in formation.grunts:
			self.addActor( grunt )

		formation = SquareFormation( 16, Vector(900,-100), DirectionMovePattern(Vector(-4,4)) )
		for grunt in formation.grunts:
			self.addActor( grunt )

		formation = SquareFormation( 9, Vector(300,0), DirectionMovePattern(Vector(0,4)) )
		for grunt in formation.grunts:
			self.addActor( grunt )