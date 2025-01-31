"""Module for the ErrorsTrigger class."""

from maps4fsbot.triggers.messages.message_base import MessageTrigger


class DockerErrorsTrigger(MessageTrigger):
    """Trigger for messages that mention errors or issues."""

    _keywords = ["error", "wsl", "docker", "engine", "can't"]
    _response = (
        "if you have issues with Docker, make sure that you have read the [docker FAQ](<https://"
        "github.com/iwatkot/maps4fs/blob/main/docs/FAQ_docker.md>) before asking for help."
    )
    _occurrences = 2
