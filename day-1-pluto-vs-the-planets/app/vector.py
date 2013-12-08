# ----------- Vector -----------
# Maths and shit
# -----------------------------


class Vector( ):

	def __init__( self, x, y ):
		self.x = float(x)
		self.y = float(y)

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

	def copy( self ):
		v = Vector( self.x, self.y )
		return v

	def unit( self ):
		u = self.copy( )
		if abs(u.x) > abs(u.y):
			u.y = u.y / u.x
			u.x = u.x / u.x
		else:
			u.x = u.x / u.y
			u.y = u.y / u.y
		return u

	def __str__( self ):
		return 'Vector: %.2f, %.2f' % ( self.x, self.y )