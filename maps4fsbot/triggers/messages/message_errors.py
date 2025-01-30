"""Module for the ErrorsTrigger class."""

from maps4fsbot.triggers.messages.message_base import MessageTrigger


class ErrorsTrigger(MessageTrigger):
    """Trigger for messages that mention errors or issues."""

    _keywords = ["error", "exception", "problem", "bug", "issue", "crash", "have"]
    _response = (
        "make sure that you have checked out the [docs](<https://github.com/iwatkot/maps4fs/tree/"
        "main/docs>) section before asking a question.\n"
        "If you asking for help, make sure, that you've provided the following information:\n"
        "- coordinates\n"
        "- size\n"
        "- rotation\n"
        "- DTM Provider\n"
        "- Local or public app version\n"
        "- All the applied settings\n"
        "- Description of the issue (including logs from the Game or from the Giants Editor)\n"
        "If you don't know how to obtain logs from Giants Editor, check this [section]"
        "(<https://github.com/iwatkot/maps4fs/blob/main/docs/FAQ.md#giants-editor-crashes-"
        "when-i-try-to-open-the-map-what-should-i-do>).\n"
        "To obtain logs from the game, check this [section](<https://github.com/iwatkot/maps4fs"
        "/blob/main/docs/FAQ.md#game-is-crashing-or-hangs-when-i-try-to-load-the-map-what-"
        "should-i-do>)."
    )
    _occurrences = 2
