# ------------------ Collision -------------------
# For register collision groups and firing events.
# ------------------------------------------------


# -------- Imports --------
# 
import pygame


# ----------- Collider -----------
# 
class Collider( ):
	def __init__( self, groupA, groupB, callback ):
		self.groupA = groupA
		self.groupB = groupB
		self.callback = callback

		self.killA = False
		self.killB = False

	def check( self ):
		collisions = pygame.sprite.groupcollide( self.groupA, self.groupB, self.killA, self.killB )
		for sprite in collisions:
			self.callback( sprite )