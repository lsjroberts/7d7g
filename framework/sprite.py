# ----------- Sprite ------------
# Handles different types of sprites.
# ----------------------------


# -------- Imports --------

import pygame, config
from app import UpdateableGameObject
from vector import Vector


# -------- Sprite --------
# Base abstract sprite
class Sprite( pygame.sprite.Sprite, UpdateableGameObject ):

    # -------- Init --------
    # Constructor
    #
    # @return Sprite
    def __init__( self ):
        self.groups = config.sprites, config.spriteGroups['all']
        pygame.sprite.Sprite.__init__( self, self.groups )

        UpdateableGameObject.__init__( self )


# -------- Static Sprite --------
# A sprite that has a single frame.
class StaticSprite( Sprite ):

    # -------- Init --------
    # Constructor
    #
    # @return StaticSprite
    def __init__( self, src, vector=Vector(0,0) ):
        Sprite.__init__( self )

        prefix = config.folders['sprites']
        for folder in config.folders:
            if folder == src[:len(folder)]:
                prefix = ''

        self.image = pygame.image.load( prefix + src ).convert_alpha( )

        self.vector = vector
        self.rect = self.image.get_rect( )
        self.rect.x, self.rect.y = self.vector.x, self.vector.y

    # -------- Update --------
    # Update the sprite's position
    def update( self, frameTime, lifeTime ):
        self.rect.x, self.rect.y = self.vector.x, self.vector.y


# -------- Animated Sprite --------
# A sprite that can have multiple frames.
class AnimatedSprite( Sprite ):

    # -------- Init --------
    # Constructor
    #
    # @return AnimatedSprite
    def __init__( self, src, vector=Vector(0,0) ):
        Sprite.__init__( self )

        self.images = []
        self.numFrames = 0
        self.states = {}
        self.loaded = False
        self.vector = vector

        prefix = config.folders['sprites']
        for folder in config.folders:
            if folder == src[:len(folder)]:
                prefix = ''

        self.srcImage = pygame.image.load( prefix + src ).convert_alpha( )
        self.srcWidth, self.srcHeight = self.srcImage.get_size( )

        self.lastUpdate = 0
        self.frame = 0
        self.state = ''

    # ----------- Add Animation State -----------
    #
    # @param  string name  State identifier name
    # @param  int    start Frame to start the animation at
    # @param  int    end   Frame to end the animation at
    # @param  int    fps   Number of frames to show per second
    # @return None
    def addAnimationState( self, name, start, end, fps ):
        self.numFrames += ( end - start + 1 )
        self.states[name] = {
            'start': start,
            'end': end,
            'delay': ( 1000 / fps )
        }

    # ----------- Load States -----------
    # Split the src image into each frame image.
    #
    # @return None
    def loadStates( self ):
        self.frameWidth = self.srcWidth / self.numFrames
        for i in range( self.numFrames ):
            subSurface = self.srcImage.subsurface( i * self.frameWidth, 0, self.frameWidth, self.srcHeight )
            self.images.append( subSurface )
        self.image = self.images[0]
        self.rect = self.image.get_rect( )
        self.rect.x, self.rect.y = self.vector.x, self.vector.y

    # ----------- Set Animation State -----------
    #
    # @param  string name State identifier name.
    # @return None
    def setAnimationState( self, name ):
        if name != self.state:
            if False == self.loaded:
                self.loadStates( )
            self.state = name
            self.frame = self.states[name]['start']
            self.lastUpdate = 0

    # ----------- Update Animation -----------
    #
    # @param  int lifeTime Number of milliseconds since pygame initialised.
    # @return None
    def updateAnimation( self, lifeTime ):
        # Get the current state
        state = self.states[self.state]

        # Update the rect vector position
        self.rect.x, self.rect.y = self.vector.x, self.vector.y

        # Check if enough time has passed since the last update for this state
        if lifeTime - self.lastUpdate > state['delay']:
            self.frame += 1

            # Wrap the frame between the state start and end frame
            if self.frame < state['start']: self.frame = state['end']
            if self.frame > state['end']: self.frame = state['start']

            # Change the sprite image to that of the current frame
            self.image = self.images[self.frame]

            # Store the update time
            self.lastUpdate = lifeTime

    # ----------- Update -----------
    def update( self, frameTime, lifeTime ):
        self.updateAnimation( lifeTime )
