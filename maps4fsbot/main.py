import discord

from maps4fsbot.config import DISCORD_TOKEN
from maps4fsbot.triggers.messages.message_base import MessageTrigger


class MyClient(discord.Client):
    async def on_ready(self):
        pass

    async def on_message(self, message):
        response = MessageTrigger.get_response(message)
        if response:
            await message.channel.send(f"{message.author.mention} {response}")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)
