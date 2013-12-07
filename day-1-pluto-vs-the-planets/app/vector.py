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

	def subtract( self, vector ):
		self.x = self.x - vector.x
		self.y = self.y - vector.y

	def dot( self, vector ):
		self.x = self.x * vector.x
		self.y = self.y * vector.y

	def divide( self, vector ):
		self.x = self.x / vector.x
		self.y = self.y / vector.y