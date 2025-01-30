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
    admin = "Admin"
    moderator = "Moderator"


class Channels:
    suggest_feature = "suggest-feature"
