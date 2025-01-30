"""Configuration for the bot."""

import os

try:
    from dotenv import load_dotenv

    load_dotenv("local.env")
except ModuleNotFoundError:
    pass

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN is not set")


class Roles:
    """Roles for the bot."""

    admin = "Admin"
    moderator = "Moderator"


class Channels:
    """Channels for the bot."""

    suggest_feature = "suggest-feature"
