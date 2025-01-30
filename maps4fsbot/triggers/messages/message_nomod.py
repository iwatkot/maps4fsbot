"""Module for the NoModTrigger class."""

from maps4fsbot.triggers.messages.message_base import MessageTrigger


class NoModTrigger(MessageTrigger):
    """Trigger for messages that mention the game can't see the map."""

    _keywords = ["no mod", "can't see map", "no map"]
    _response = (
        "if the game can not see your map, check out this [section](<https://github.com/iwatkot"
        "/maps4fs/blob/main/docs/FAQ.md#the-game-cant-see-the-map-mod-what-should-i-do>)."
    )
    _occurrences = 1
