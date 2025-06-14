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

SECRET_SALT = os.getenv("SECRET_SALT")
if not SECRET_SALT:
    raise ValueError("SECRET_SALT is not set")


class Roles:
    """Roles for the bot."""

    admin = "Admin"
    moderator = "Moderator"


class Channels:
    """Channels for the bot."""

    suggest_feature = "suggest-feature"
