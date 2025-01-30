from maps4fsbot.triggers.messages.message_base import MessageTrigger


class QgisTrigger(MessageTrigger):
    _keywords = ["qgis", "QGIS"]
    _response = (
        "downloading satellite images using QGIS is deprecated, the generator can download images "
        "by itself now, check out the Satellite settings section."
    )
    _occurrences = 1
