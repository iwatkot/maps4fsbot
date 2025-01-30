import discord

from maps4fsbot.config import DISCORD_TOKEN


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")
        # Reply to the message

        if message.content == "ping":
            await message.channel.send("pong")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)
