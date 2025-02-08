"""Main file for the bot."""

import discord
from discord.ext import commands
from discord.ext.commands.context import Context

from maps4fsbot.config import DISCORD_TOKEN
from maps4fsbot.templates import Messages
from maps4fsbot.triggers.messages.message_base import MessageTrigger

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)


@bot.event
async def on_message(message: discord.Message) -> None:
    """Event handler for when a message is sent in a channel the bot can see.

    Arguments:
        message (discord.Message): The message that was sent in a channel the bot can see.
    """
    if message.channel.name == "welcome":  # type: ignore
        if "Unverified" in [role.name for role in message.author.roles]:  # type: ignore
            if message.content.lower().strip() == Messages.user_check_answer:
                role = discord.utils.get(message.guild.roles, name="Unverified")  # type: ignore
                await message.author.remove_roles(role)  # type: ignore
                await message.channel.send(f"{message.author.mention} {Messages.welcome}")
                return

    response = MessageTrigger.get_response(message)
    if response:
        await message.channel.send(f"{message.author.mention} {response}")
    await bot.process_commands(message)


@bot.event
async def on_member_join(member: discord.Member) -> None:
    """Event handler for when a new member joins the server.

    Arguments:
        member (discord.Member): The member that joined the server.
    """
    channel = discord.utils.get(member.guild.text_channels, name="welcome")
    if channel:
        await channel.send(f"{member.mention} {Messages.user_check}")
        role = discord.utils.get(member.guild.roles, name="Unverified")
        await member.add_roles(role)  # type: ignore


@bot.command()
async def docs(ctx: Context) -> None:
    """Sends a link to the documentation."""
    await ctx.send(Messages.docs)


@bot.command()
async def schema(ctx: Context) -> None:
    """Sends a link to the texture schema."""
    await ctx.send(Messages.schema)


@bot.command()
async def settings(ctx: Context) -> None:
    """Sends a link to the advanced settings."""
    await ctx.send(Messages.settings)


@bot.command()
async def expert(ctx: Context) -> None:
    """Sends a link to the expert settings."""
    await ctx.send(Messages.expert)


@bot.command()
async def debugge(ctx: Context) -> None:
    """Sends a link to the instructions for debugging Giants Editor."""
    await ctx.send(Messages.debugge)


@bot.command()
async def debuggame(ctx: Context) -> None:
    """Sends a link to the instructions for debugging the Farming Simulator game."""
    await ctx.send(Messages.debuggame)


@bot.command()
async def structure(ctx: Context) -> None:
    """Sends a link to the instructions for correct file structure."""
    await ctx.send(Messages.structure)


@bot.command()
async def faq(ctx: Context) -> None:
    """Sends a link to the FAQ."""
    await ctx.send(Messages.faq)


@bot.command()
async def dockerfaq(ctx: Context) -> None:
    """Sends a link to the Docker FAQ."""
    await ctx.send(Messages.docker_faq)


bot.run(DISCORD_TOKEN)  # type: ignore
