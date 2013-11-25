# ----------- Actor ------------
# Actors represent interactable characters within the game world.
# ----------------------------


# -------- Imports --------

import config


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

    def move( self, vector ):
        self.moveVector = vector

    def update( self, frameTime, lifeTime ):
        self.vector = self.vector.add( self.moveVector )

        Actor.update( self, frameTime, lifeTime )


# ----------- Controllable Actor -----------
# An actor that can be positioned.
class ControllableActor( MoveableActor ):

    def setSpeed( self, speed ):
        self.speed = speed

    # ----------- Set Target -----------
    # Set the actor's target
    # 
    # @param  Vector vector
    # @return None
    def setTargetVector( self, vector ):
        self.targetVector = vector

    def update( self, frameTime, lifeTime ):
        pass


# ----------- Conversational Actor -----------
# An actor who can hold a conversation.
class ConversationalActor( Actor ):
    pass


# ----------- Emotional Actor -----------
# An actor who has emotions and reactions.
class EmotionalActor( Actor ):
    
    def addEmotion( self, emotion ):
        if self.emotions is None:
            self.emotions = {}

        self.emotions[emotion.name] = emotion

    def addTargetedEmotion( self, emotion, target ):
        if self.targetedEmotions is None:
            self.targetedEmotions = {}

        if self.targetedEmotions[target.name] is None:
            self.targetedEmotions[target.name] = {}

        self.targetedEmotions[target.name][emotion.name] = emotion