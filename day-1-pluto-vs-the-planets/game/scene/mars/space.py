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
from game.actor.grunt import SquareFormation, DiamondFormation, DirectionMovePattern

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

		def addSquare(data):
			SquareFormation( data['num'], data['vector'], DirectionMovePattern(data['moveVector']) )

		def addDiamond(data):
			DiamondFormation( data['num'], data['vector'], DirectionMovePattern(data['moveVector']) )

		self.addTimingCallback( 2, addSquare, {'num': 9,  'vector': Vector(100, -100), 'moveVector': Vector(1,2)} )
		self.addTimingCallback( 4, addSquare, {'num': 16, 'vector': Vector(900, -200), 'moveVector': Vector(-2,2)} )
		self.addTimingCallback( 4, addDiamond, {'num': 9,  'vector': Vector(300, -100), 'moveVector': Vector(0,2)} )
		self.addTimingCallback( 7, addDiamond, {'num': 25,  'vector': Vector(400, -300), 'moveVector': Vector(0,2)} )

	def update( self, frameTime, lifeTime ):
		VerticalScrollingScene.update( self, frameTime, lifeTime )
		TimingScene.update( self, frameTime, lifeTime )