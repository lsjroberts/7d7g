# ---------- Event -----------
# Handles event listening and firing.
# ----------------------------


# -------- Event Manager --------
# Handles registering listeners and notifying them of events.
class EventManager( ):

    # -------- Init --------
    # Construct the event manager with an empty set of listeners.
    #
    # @return None
    def __init__( self ):
        self.listeners = [ ]

    # -------- Register Listener --------
    # Add a listener if it has not already been registered.
    #
    # @param  EventListener
    # @return bool
    def registerListener( self, listener ):
        if listener in self.listeners:
            return False
        self.listeners.append( listener )
        return True

    # -------- Un-Register Listener --------
    # Remove a listener from the event manager.
    #
    # @return None
    def unRegisterListener( self, listener ):
        pass

    # -------- Post --------
    # Post the event to every listener.
    #
    # @param  Event
    # @return None
    def post( self, event ):
        for listener in self.listeners:
            listener.notify( event )


# -------- Event Listener --------
# Superclass for any event listeners.
class EventListener( ):

    # -------- Notify --------
    # Check and handle an event.
    #
    # @param  Event
    # @return None
    def notify( self, event ):
        raise NotImplementedError( 'You must implement a notify method on the event listener' )


# -------- Event --------
# Superclass for any events that might be generated for an object and sent to
# the event manager.
class Event( ):
    name = 'generic'

    # -------- Init --------
    # Construct the event and set it's data.
    #
    # @param  mixed data Any optional data to add to the event.
    # @return Event
    def __init__( self, data=None ):
        self.data = data


# -------- Pygame Event --------
# Generic pygame event
class PygameEvent( Event ):
    name = 'pygame'