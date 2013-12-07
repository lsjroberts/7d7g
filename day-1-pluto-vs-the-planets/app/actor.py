# ----------- Actor ------------
# Actors represent interactable characters within the game world.
# ----------------------------


# -------- Imports --------

import pygame, config
from event import EventListener, PygameEvent
from vector import Vector


# -------- Actor --------
# Base abstract actor
class Actor( ):

    # -------- Init --------
    # Constructor
    #
    # @return Actor
    def __init__( self ):
        self.sprite = None
        self.vector = Vector( 0,0 )

    def setSprite( self, sprite ):
        self.sprite = sprite

    def update( self, frameTime, lifeTime ):
        self.sprite.vector = self.vector


# ----------- Moveable Actor -----------
# An actor that can be repositioned after instantiation.
class MoveableActor( Actor ):

    def __init__( self ):
        Actor.__init__( self )

        self.moveVector = Vector( 0, 0 )

    def move( self, vector ):
        self.moveVector = vector

    def update( self, frameTime, lifeTime ):
        self.vector = self.vector.add( self.moveVector )

        Actor.update( self, frameTime, lifeTime )


# ----------- Controllable Actor -----------
# An actor that can be positioned.
class ControllableActor( MoveableActor ):

    def __init__( self ):
        MoveableActor.__init__( self )

        self.speed = 0
        self.targetVector = Vector( 0, 0 )
        self.controls = []

        config.app.events.registerListener( ActorListener(self) )

    def setSpeed( self, speed ):
        self.speed = speed

    # ----------- Set Target -----------
    # Set the actor's target
    # 
    # @param  Vector vector
    # @return None
    def setTargetVector( self, vector ):
        self.targetVector = vector

    def addControlHold( self, key, callback ):
        self.controls.append({
            'type': pygame.KEYDOWN,
            'key': key,
            'callback': callback
        })

    def update( self, frameTime, lifeTime ):
        pass


# ----------- Actor Listener -----------
# Listener with associated actor
class ActorListener( EventListener ):

    def __init__( self, actor ):
        self.actor = actor

    def notify( self, event ):
        if isinstance( event, PygameEvent ):
            for control in self.actor.controls:
                if control['type'] == event.data.type and control['key'] == event.data.key:
                    control['callback']()