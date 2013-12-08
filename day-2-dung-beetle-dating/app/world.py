# ----------- World -----------
# Handles world logic
# -----------------------------


# ----------- World -----------
# 
class World( ):

	def __init__( self ):
		self.scene = None

	def setScene( self, scene ):
		if self.scene is not None:
			self.unloadScene( )
		self.scene = scene

	def unloadScene( self ):
		if self.scene is None:
			raise Exception( 'Can not unload scene, none set' )
		self.scene = None