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
        "Please, read the [FAQ](<https://maps4fs.gitbook.io/docs/getting-started/faq>) "
        "before asking any questions. \n"
        "💬 **NEW**: Ask me questions by tagging @maps4fsbot followed by your question!\n\n"
        "📥 **NEW**: Download the standalone [Windows app](<https://maps4fs.xyz/download>), no Docker required!\n\n"
        "⚠️ Carefully read the [Get Help](<https://maps4fs.gitbook.io/docs/setup-and-installation/get_help>) documentation "
        "before asking for help. Requests without following the guide may be ignored.\n"
        "Support the project at [BuyMeACoffee](<https://www.buymeacoffee.com/iwatkot>) "
        "or [Patreon](<https://www.patreon.com/iwatkot>).\n"
        "It's also recommended to check out the YouTube tutorials in this [playlist]"
        "(<https://www.youtube.com/playlist?list=PLug0g7UYHX8D1Jik6NkJjQhdxqS-NOtB9>) "
        "and get familiar with other [docs](<https://maps4fs.gitbook.io/docs>).\n"
        "If you're planning to report a bug, read the pinned message in the "
        "`#bug-reports` channel first. Incorrectly formatted bug reports will be deleted.\n"
        "If the issue is related to the DTM Provider, please note that the author of the "
        "tool maintaining only the SRTM provider, all other DTM Providers are "
        "community maintained and may not work properly. In this case, "
        "you can try to ask the author of the specific DTM Provider for help.\n\n"
        "Useful links:\n"
        "- [pydtmdl](<https://github.com/iwatkot/pydtmdl>) - list of available DTM Providers with "
        "their authors.\n"
        "- [How to use Maps4FS effectively](<https://maps4fs.gitbook.io/docs/getting-started/workflow_optimizations>)\n"
    )

    docs = "Here's a link to the [docs](<https://maps4fs.gitbook.io/docs>) section."

    schema = "Here's a link to the [texture schema](<https://maps4fs.gitbook.io/docs/understanding-the-basics/texture_schema>) explanation."

    settings = "Here's a link to the [generation settings](<https://maps4fs.gitbook.io/docs/understanding-the-basics/generation_settings>) of the generator."

    debugge = (
        "Here's a link to the [debugging](<https://maps4fs.gitbook.io/docs/getting-started/faq#giants-editor-crashes-when-opening-map>) instructions "
        "for Giants Editor."
    )

    debuggame = (
        "Here's a link to the [debugging](<https://maps4fs.gitbook.io/docs/getting-started/faq#game-crashes-or-hangs-when-loading-map>) "
        "instructions for the Farming Simulator game."
    )

    structure = "Here's a link to the [correct file structure](<https://maps4fs.gitbook.io/docs/getting-started/faq#mod-installation-issues>) for the mod archive."

    faq = "Here's a link to the [FAQ](<https://maps4fs.gitbook.io/docs/getting-started/faq>)."

    apikey_sent = "Your API key has been sent to you in a private message."
    apikey_error = (
        "I can't send you a private message. "
        "Please check your privacy settings and allow direct messages from server members."
    )
    local_docs = "Here's a link to the [Local Deployment Documentation](<https://maps4fs.gitbook.io/docs/setup-and-installation/local_deployment>)."
    local_troubleshoot = "Here's a link to the [Local Troubleshooting Guide](<https://maps4fs.gitbook.io/docs/setup-and-installation/local_deployment#troubleshooting>)."

    get_help = "Here's a link to the [Get Help](<https://maps4fs.gitbook.io/docs/setup-and-installation/get_help>)."
