"""Templates for the bot messages."""


class Messages:
    """Templates for the bot messages."""

    user_check = (
        "please reply to this message with the name of the tool about which this Discord server "
        "is dedicated to access the rest of the server.\n"
        "Unless you do this, you won't be able to see the rest of the channels."
    )

    user_check_answer = "maps4fs"

    welcome = (
        "welcome to the maps4fs Dicord server!\nGet familiar with the [docs](<https://"
        "github.com/iwatkot/maps4fs/tree/main/docs>) before asking any questions."
    )

    docs = (
        "Here's a link to the [docs](<https://github.com/iwatkot/maps4fs/tree/main/docs>) section."
    )

    schema = (
        "Here's a link to the [texture schema](<https://github.com/iwatkot/maps4fs/blob/main/"
        "README.md#Texture-schema>) explanation."
    )

    settings = (
        "Here's a link to the [advanced settings](<https://github.com/iwatkot/maps4fs/blob/main/"
        "README.md#Advanced-settings>) of the generator."
    )

    expert = (
        "Here's a link to the [expert settings](<https://github.com/iwatkot/maps4fs/blob/main/"
        "README.md#Expert-settings>) of the generator."
    )

    debugge = (
        "Here's a link to the [debugging](<https://github.com/iwatkot/maps4fs/blob/main/docs/"
        "FAQ.md#giants-editor-crashes-when-i-try-to-open-the-map-what-should-i-do>) instructions "
        "for Giants Editor."
    )

    debuggame = (
        "Here's a link to the [debugging](<https://github.com/iwatkot/maps4fs/blob/main/docs/"
        "FAQ.md#game-is-crashing-or-hangs-when-i-try-to-load-the-map-what-should-i-do>) "
        "instructions for the Farming Simulator game."
    )

    structure = (
        "Here's a link to the [correct file structure](<https://github.com/iwatkot/maps4fs/blob/"
        "main/docs/FAQ.md#the-game-cant-see-the-map-mod-what-should-i-do>) for the mod archive."
    )

    faq = "Here's a link to the [FAQ](<https://github.com/iwatkot/maps4fs/blob/main/docs/FAQ.md>)."
    docker_faq = (
        "Here's a link to the [Docker FAQ](<https://github.com/iwatkot/maps4fs/blob/main/"
        "docs/FAQ_docker.md>)."
    )

    apikey_sent = "Your API key has been sent to you in a private message."
    apikey_error = (
        "I can't send you a private message. "
        "Please check your privacy settings and allow direct messages from server members."
    )
