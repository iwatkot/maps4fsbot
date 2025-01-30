"""Message trigger for angle-based unwrap method."""

from maps4fsbot.triggers.messages.message_base import MessageTrigger


class AngleBasedTrigger(MessageTrigger):
    """Trigger for messages that mention the angle-based unwrap method."""

    _keywords = ["angle-based", "angle based"]
    _response = (
        "if the angle-based unwrap is not working or working incorrectly, you can also use the "
        "Project from view (bounds) unwrap method.\n"
        "Ensure that you're on a Top view (Numpad 7) and press U -> Project from view (bounds)."
    )
    _occurrences = 1
