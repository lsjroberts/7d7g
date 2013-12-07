# ---------- Timing Scene --------------
# Scenes that can have delayed actions
# on a timer.
# --------------------------------------

# -------- Imports --------

from app.app import UpdateableGameObject
from app.scene import Scene


# ----------- Timing Scene -----------
#
class TimingScene( Scene, UpdateableGameObject ):
	def __init__( self, verticalSpeed=0 ):
		Scene.__init__( self )
		UpdateableGameObject.__init__( self )

		self.timingCallbacks = []

	def addTimingCallback( self, time, callback, data ):
		self.timingCallbacks.append({
			'time': time,
			'callback': callback,
			'data': data
		})

	def update( self, frameTime, lifeTime ):
		seconds = lifeTime / 1000

		for callback in self.timingCallbacks:
			if callback['time'] == seconds:
				callback['callback'](callback['data'])
				self.timingCallbacks.remove(callback)