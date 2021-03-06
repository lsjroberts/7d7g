# ---------- Scene - Mars -----------
# 
# -----------------------------------

# -------- Imports --------

import app.config as config
from app.scene import SceneLayer
from app.vector import Vector
from game.scene.scrolling import VerticalScrollingScene, HorizontalScrollingScene
from game.scene.timing import TimingScene
from game.actor.pluto import Pluto
from game.actor.grunt import SquareFormation, DiamondFormation, SpiralFormation, DirectionMovePattern

# ----------- Mars Scene -----------
# 
class Space( VerticalScrollingScene, HorizontalScrollingScene, TimingScene ):

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

		def addSpiral(data):
			SpiralFormation( data['num'], data['vector'], DirectionMovePattern(data['moveVector']) )


		w = config.settings['game_w']

		self.addTimingCallback(  2, addSquare,  {'num':  9, 'vector': Vector(.1*w, -100), 'moveVector': Vector(1,2)} )
		self.addTimingCallback(  4, addDiamond, {'num': 16, 'vector': Vector(.9*w, -200), 'moveVector': Vector(-2,2)} )
		self.addTimingCallback(  4, addSquare,  {'num':  9, 'vector': Vector(.3*w, -100), 'moveVector': Vector(0,2)} )
		self.addTimingCallback(  7, addSpiral,  {'num': 30, 'vector': Vector(.4*w, -300), 'moveVector': Vector(0,2)} )
		self.addTimingCallback( 15, addSquare,  {'num': 40, 'vector': Vector(.4*w, -400), 'moveVector': Vector(0,4)} )
		self.addTimingCallback( 20, addSpiral,  {'num': 30, 'vector': Vector(.2*w, -300), 'moveVector': Vector(2,2)} )
		self.addTimingCallback( 20, addSpiral,  {'num': 30, 'vector': Vector(.6*w, -300), 'moveVector': Vector(-2,2)} )
		self.addTimingCallback( 22, addDiamond, {'num':  4, 'vector': Vector(.2*w, -100), 'moveVector': Vector(0,2)} )
		self.addTimingCallback( 26, addDiamond, {'num':  9, 'vector': Vector(.4*w, -100), 'moveVector': Vector(0,1)} )
		self.addTimingCallback( 27, addSquare,  {'num':  9, 'vector': Vector(.3*w, -100), 'moveVector': Vector(0,3)} )
		self.addTimingCallback( 33, addSpiral,  {'num': 16, 'vector': Vector(.7*w, -300), 'moveVector': Vector(-3,3)} )

		j = 1.0
		for i in range(36, 44):
			self.addTimingCallback( i, addDiamond, {'num':  4, 'vector': Vector((j/10)*w, -100), 'moveVector': Vector(0,3)} )
			j += 1

		j = 1.0
		for i in range(45, 54):
			self.addTimingCallback( i, addSquare, {'num':  2, 'vector': Vector((j/10)*w, -100), 'moveVector': Vector(0,12)} )
			self.addTimingCallback( i, addSquare, {'num':  2, 'vector': Vector((1-(j/10))*w, -100), 'moveVector': Vector(0,12)} )
			j += 1

		self.addTimingCallback( 60, addSpiral,  {'num': 60, 'vector': Vector(.5*w, -400), 'moveVector': Vector(0,1)} )

	def update( self, frameTime, lifeTime ):
		VerticalScrollingScene.update( self, frameTime, lifeTime )
		HorizontalScrollingScene.update( self, frameTime, lifeTime )
		TimingScene.update( self, frameTime, lifeTime )