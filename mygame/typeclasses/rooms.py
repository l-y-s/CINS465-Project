"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from evennia import search_object
import time

class Room(DefaultRoom):
    """
    Rooms are like any Object, except their location is None
    (which is default). They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)

    See examples/object.py for a list of
    properties and methods available on all Objects.
    """
    pass

class DreamRoom(DefaultRoom):
    """
    This room acts as an interim room which automatically
    teleports you to a different room after a certain amount of time.
    """

    def at_object_creation(self):
        super(DreamRoom, self).at_object_creation()
        self.db.teleport_to = "inn bedroom"
        self.db.desc = """|cDreamscape|n|/You are standing in an endless, black expanse. You feel as though you've been there forever and at the same time a very short while. As you continue to look around, a single pinpoint of light sparks to life in the distance in front of you. Suddenly, you being gliding toward the light without walking. The light grows larger as you approach, and you start realizing how tired you feel...|/|/And then you wake up..."""

    def at_object_receive(self, character, source_location):
        """
        This hook is called by the engine whenever the player is moved into this room.
        """

        if not character.has_account:
            # only act on player characters.
            return
        teleport_to = self.db.teleport_to
        results = search_object(teleport_to)
        character.msg(self.db.desc)
        if not results or len(results) > 1:
            character.msg("no valid teleport target for %s was found." % teleport_to)
            return
        if character.is_superuser:
            # superusers don't get teleported
            character.msg("Superuser block: You would have been teleported to %s." % results[0])
            return
        # perform the teleport
        character.move_to(results[0], quiet=True, move_hooks=False)
        results[0].at_object_receive(character, self)
