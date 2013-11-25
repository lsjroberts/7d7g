# ------------ NPC ------------
# Non-playable characters
# -----------------------------


# -------- Imports --------

import config
from actor import MoveableActor, ConversationalActor, EmotionalActor


# ----------- NPC -----------
# Abstract NPC
class NPC( MoveableActor ):
	pass


# ----------- Conversational NPC -----------
# NPC with whom the player can converse.
class ConversationalNPC( NPC, ConversationalActor ):
	pass


# ----------- Emotional NPC -----------
# NPC who can react emotionally to the player.
class EmotionalNPC( NPC, EmotionalActor ):
	pass