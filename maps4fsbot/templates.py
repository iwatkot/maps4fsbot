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
        ", welcome to the maps4fs Dicord server!\n"
        "You can now access the rest of the channels.\n"
        "The public version of the app is here: [maps4fs.xyz](<https://maps4fs.xyz>).\n"
        "Please, read the [FAQ](<https://github.com/iwatkot/maps4fs/blob/main/docs/FAQ.md>) "
        "and the [Docker FAQ](<https://github.com/iwatkot/maps4fs/blob/main/docs/FAQ_docker.md>) "
        "before asking any questions. \n"
        "⚠️ Check out detailed [Local Deployment](<https://github.com/iwatkot/maps4fs/blob/main/docs/local_deployment.md>) instructions "
        "to run the tool locally.\n"
        "⚠️ Carefully read the [Get Help](<https://github.com/iwatkot/maps4fs/blob/main/docs/get_help.md>) documentation "
        "before asking for help. Requests without following the guide may be ignored.\n"
        "Support the project at [BuyMeACoffee](<https://www.buymeacoffee.com/iwatkot>) "
        "or [Patreon](<https://www.patreon.com/iwatkot>).\n"
        "It's also recommended to check out the YouTube tutorials in this [playlist]"
        "(<https://www.youtube.com/playlist?list=PLug0g7UYHX8D1Jik6NkJjQhdxqS-NOtB9>) "
        "and get familiar with other [docs](<https://github.com/iwatkot/maps4fs/tree/main/docs>).\n"
        "If you're planning to report a bug, read the pinned message in the "
        "`#bug-reports` channel first. Incorrectly formatted bug reports will be deleted.\n"
        "If the issue is related to the DTM Provider, please note that the author of the "
        "tool maintaining only the SRTM provider, all other DTM Providers are "
        "community maintained and may not work properly. In this case, "
        "you can try to ask the author of the specific DTM Provider for help.\n\n"
        "Useful links:\n"
        "- [Maps4FS API](<https://github.com/iwatkot/maps4fsapi>). If you need an API key for the "
        "public version of the app, check out the `#api-keys` channel.\n"
        "- [pydtmdl](<https://github.com/iwatkot/pydtmdl>) - list of available DTM Providers with "
        "their authors.\n"
        "- [How to use Maps4FS effectively](<https://github.com/iwatkot/maps4fs/blob/main/docs/recommendations.md>)\n"
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
    local_docs = "Here's a link to the [Local Deployment Documentation](<https://github.com/iwatkot/maps4fs/blob/main/docs/local_deployment.md>)."
    local_troubleshoot = "Here's a link to the [Local Troubleshooting Guide](<https://github.com/iwatkot/maps4fs/blob/main/docs/local_deployment.md#troubleshooting>)."

    get_help = "Here's a link to the [Get Help](<https://github.com/iwatkot/maps4fs/blob/main/docs/get_help.md>)."
