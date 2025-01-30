from maps4fsbot.triggers.messages.message_base import MessageTrigger


class ErrorsTrigger(MessageTrigger):
    _keywords = ["error", "exception"]
    _response = (
        "I'm sorry, I cannot help you with that. Please contact the developer for assistance."
    )
    _timeout = 60
    # _exclude_channels = ["bot-commands"]
    # _exclude_roles = ["Admin"]
    _occurrences = 1
