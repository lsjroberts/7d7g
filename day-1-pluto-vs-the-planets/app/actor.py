# ----------- Actor ------------
# Actors represent interactable characters within the game world.
# ----------------------------


# -------- Imports --------

import pygame, config
from app import UpdateableGameObject
from event import EventListener, PygameEvent
from vector import Vector


# -------- Actor --------
# Base abstract actor
class Actor( UpdateableGameObject ):

    # -------- Init --------
    # Constructor
    #
    # @return Actor
    def __init__( self ):
        UpdateableGameObject.__init__( self )

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

    def moveLeft( self ):
        self.move( self.moveVector.add(
            Vector( -self.speed, 0 )
        ))

    def moveRight( self ):
        self.move( self.moveVector.add(
            Vector( self.speed, 0 )
        ))

    def moveUp( self ):
        self.move( self.moveVector.add(
            Vector( 0, -self.speed )
        ))

    def moveDown( self ):
        self.move( self.moveVector.add(
            Vector( 0, self.speed )
        ))

    def stopLeft( self ):
        self.move( self.moveVector.add(
            Vector( self.speed, 0 )
        ))

    def stopRight( self ):
        self.move( self.moveVector.add(
            Vector( -self.speed, 0 )
        ))

    def stopUp( self ):
        self.move( self.moveVector.add(
            Vector( 0, self.speed )
        ))

    def stopDown( self ):
        self.move( self.moveVector.add(
            Vector( 0, -self.speed )
        ))

    def update( self, frameTime, lifeTime ):
        self.vector.add( self.moveVector )
        
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

    def addControl( self, key, callback, keyType ):
        self.controls.append({
            'type': keyType,
            'key': key,
            'callback': callback
        })

    def addControlDown( self, key, callback ):
        self.addControl( key, callback, pygame.KEYDOWN )

    def addControlUp( self, key, callback ):
        self.addControl( key, callback, pygame.KEYUP )

    def update( self, frameTime, lifeTime ):
        MoveableActor.update( self, frameTime, lifeTime )


# ----------- AI Actor -----------
# Actor controlled by the computer
class AIActor( MoveableActor ):
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