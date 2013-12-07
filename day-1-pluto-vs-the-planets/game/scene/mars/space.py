# ---------- Scene - Mars -----------
# 
# -----------------------------------

# -------- Imports --------

import app.config as config
from app.scene import SceneLayer
from app.vector import Vector
from game.scene.scrolling import VerticalScrollingScene
from game.scene.timing import TimingScene
from game.actor.pluto import Pluto
from game.actor.grunt import SquareFormation
from game.actor.grunt import DirectionMovePattern

# ----------- Mars Scene -----------
# 
class Space( VerticalScrollingScene, TimingScene ):

	def __init__( self ):
		VerticalScrollingScene.__init__( self, .5 )
		TimingScene.__init__( self )

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

		def f1():
			SquareFormation( 9, Vector(100,0), DirectionMovePattern(Vector(1,2)) )

		def f2():
			SquareFormation( 16, Vector(900,0), DirectionMovePattern(Vector(-2,2)) )

		def f3():
			SquareFormation( 9, Vector(300,0), DirectionMovePattern(Vector(0,2)) )

		self.addTimingCallback( 2, f1 )
		self.addTimingCallback( 4, f2 )
		self.addTimingCallback( 4, f3 )

	def update( self, frameTime, lifeTime ):
		VerticalScrollingScene.update( self, frameTime, lifeTime )
		TimingScene.update( self, frameTime, lifeTime )