"""Main file for the bot."""

import discord

from maps4fsbot.config import DISCORD_TOKEN
from maps4fsbot.templates import Messages
from maps4fsbot.triggers.messages.message_base import MessageTrigger


class MyClient(discord.Client):
    """Custom client for the bot."""

    async def on_message(self, message: discord.Message) -> None:
        """Event handler for when a message is sent in a channel the bot can see.

        Arguments:
            message (discord.Message): The message that was sent in a channel the bot can see.
        """
        response = MessageTrigger.get_response(message)
        if response:
            await message.channel.send(f"{message.author.mention} {response}")

    async def on_member_join(self, member: discord.Member) -> None:
        """Event handler for when a new member joins the server.

        Arguments:
            member (discord.Member): The member that joined the server.
        """
        channel = discord.utils.get(member.guild.text_channels, name="welcome")
        if channel:
            await channel.send(f"{member.mention} {Messages.welcome}")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)  # type: ignore
client.run(DISCORD_TOKEN)  # type: ignore
