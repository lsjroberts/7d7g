# ----------- Scene -----------
# Handles scene logic
# -----------------------------


# -------- Imports --------

import config
from sprite import StaticSprite

from vector import Vector


# ----------- Scene -----------
# A scene comprised of a set of layers.
class Scene( ):

	def __init__( self ):
		self.layers = []
		self.floors = []
		self.actors = []

	def addLayer( self, layer ):
		self.layers.append( layer )

	def setFloor( self, percentage ):
		self.floors = [ SceneFloor( percentage ) ]

	def getFloor( self ):
		return self.floors[0]

	def addFloor( self, percentage ):
		self.floors.append( percentage )

	def addActor( self, actor ):
		self.actors.append( actor )
		self.getFloor( ).anchorActor( actor )



# ----------- Scene Layer -----------
# A layer image with depth position in the scene.
class SceneLayer( StaticSprite ):

	def __init__( self, src, depth ):
		StaticSprite.__init__( self, config.folders['scenes'] + src )
		self.depth = depth


# ----------- Scene Floor -----------
# 
class SceneFloor( ):

	def __init__( self, percentage ):
		self.percentage = percentage
		self.vector = Vector( 0, config.settings['screen_h'] * percentage )

	def anchorActor( self, actor ):
		actor.sprite.vector.y = self.vector.y - actor.sprite.rect.height