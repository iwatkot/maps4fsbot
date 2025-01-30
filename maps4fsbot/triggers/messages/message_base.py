from __future__ import annotations

from discord import Message

from maps4fsbot.triggers.trigger_base import TriggerBase


class MessageTrigger(TriggerBase):
    _keywords: list[str] = []
    _occurrences: int = 1
    _exclude_channels: list[str] = []
    _exclude_roles: list[str] = []
    _response: str | None = None
    _timeout: int = 0
    _last_triggered: int = 0

    @property
    def keywords(self) -> list[str]:
        """Returns the keywords that will trigger the response.

        Returns:
            list[str]: The keywords that will trigger the response.
        """
        return self._keywords

    @property
    def occurrences(self) -> int:
        """Returns the number of times the keywords must be found in the message to trigger the
            response.

        Returns:
            int: The number of times the keywords must be found in the message to trigger the
                response.
        """
        return self._occurrences

    @property
    def exclude_channels(self) -> list[str]:
        """Returns the channels that will not trigger the response.

        Returns:
            list[str]: The channels that will not trigger the response.
        """
        return self._exclude_channels

    @property
    def exclude_roles(self) -> list[str]:
        """Returns the roles that will not trigger the response.

        Returns:
            list[str]: The roles that will not trigger the response.
        """
        return self._exclude_roles

    @property
    def response(self) -> str | None:
        """Returns the response that will be sent when the keywords are found in the message.

        Returns:
            str | None: The response that will be sent when the keywords are found in the message.
        """
        return self._response

    @property
    def timeout(self) -> int:
        """Returns the timeout for the trigger, which is the time in seconds that must pass before
            the trigger can be triggered again.

        Returns:
            int: The timeout for the trigger.
        """
        return self._timeout

    @property
    def last_triggered(self) -> int:
        """Returns the epoch time the trigger was last triggered.

        Returns:
            int: The time the trigger was last triggered.
        """
        return self._last_triggered

    @classmethod
    def get_subclasses(cls) -> list[type[MessageTriggerBase]]:
        """Returns a list of all subclasses of the class.

        Returns:
            list[type[MessageTriggerBase]]: A list of all subclasses of the class.
        """
        return cls.__subclasses__()

    @classmethod
    def trigger(cls, message: Message) -> bool:
        """Checks if the message contains the keywords and if the trigger should be
            triggered.

        Arguments:
            message (Message): The message to check.

        Returns:
            bool: True if the trigger should be triggered, False otherwise.
        """
        if cls._last_triggered + cls._timeout > message.created_at.timestamp():
            return False

        if message.channel.name in cls._exclude_channels:
            return False

        for role in message.author.roles:
            if role.name in cls._exclude_roles:
                return False

        count = 0
        for keyword in cls._keywords:
            count += message.content.lower().count(keyword.lower())
            if count >= cls._occurrences:
                cls._last_triggered = message.created_at.timestamp()
                return True

        return False

    @classmethod
    def get_response(cls, message: Message) -> str | None:
        """Processes the message and returns the response if the trigger should be triggered.

        Arguments:
            message (Message): The message to process.

        Returns:
            str | None: The response if the trigger should be triggered, None otherwise.
        """
        for trigger in cls.get_subclasses():
            if trigger().trigger(message):
                return trigger().response
