# ----------- Vector -----------
# Maths and shit
# -----------------------------


class Vector( ):

	def __init__( self, x, y ):
		self.x = x
		self.y = y

	def add( self, vector ):
		self.x = self.x + vector.x
		self.y = self.y + vector.y
		return self

	def subtract( self, vector ):
		self.x = self.x - vector.x
		self.y = self.y - vector.y
		return self

	def dot( self, vector ):
		self.x = self.x * vector.x
		self.y = self.y * vector.y
		return self

	def divide( self, vector ):
		self.x = self.x / vector.x
		self.y = self.y / vector.y
		return self

	def __str__( self ):
		return 'Vector: %d, %d' % ( self.x, self.y )