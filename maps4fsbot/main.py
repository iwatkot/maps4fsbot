"""Main file for the bot."""

import discord
from discord.ext import commands
from discord.ext.commands.context import Context

from maps4fsbot.api_key import generate_api_key
from maps4fsbot.config import DISCORD_TOKEN
from maps4fsbot.llm_answer import answer_question
from maps4fsbot.templates import Messages

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
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    try:
        if message.channel.name == "welcome":  # type: ignore
            if "Unverified" in [role.name for role in message.author.roles]:  # type: ignore
                if message.content.lower().strip() == Messages.user_check_answer:
                    role = discord.utils.get(message.guild.roles, name="Unverified")  # type: ignore
                    await message.author.remove_roles(role)  # type: ignore
                    await message.channel.send(f"{message.author.mention} {Messages.welcome}")
                    return
    except Exception as e:
        print(f"Error processing message in welcome channel: {e}")

    # Check if the bot was mentioned and respond with LLM
    try:
        if bot.user.mentioned_in(message):  # type: ignore
            try:
                # Extract the question by removing the bot mention
                question = message.content
                for mention in message.mentions:
                    if mention == bot.user:
                        question = question.replace(f"<@{mention.id}>", "").replace(
                            f"<@!{mention.id}>", ""
                        )

                question = question.strip()

                if (
                    question
                ):  # Only respond if there's actually a question after removing the mention
                    # Show typing indicator while processing
                    async with message.channel.typing():
                        answer = answer_question(question)

                    # Split long answers if they exceed Discord's message limit
                    if len(answer) > 2000:
                        chunks = [answer[i : i + 1900] for i in range(0, len(answer), 1900)]
                        for chunk in chunks:
                            await message.channel.send(chunk)
                    else:
                        await message.channel.send(answer)

            except Exception as e:
                print(f"Error processing LLM question: {e}")
                await message.channel.send(
                    "Sorry, I encountered an error while processing your question."
                )
    except Exception as e:
        print(f"Error checking bot mention: {e}")

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
async def apikey(ctx: Context) -> None:
    """Generates a new API key for the user and sends as a private message.
    This command can only be used in the "api-keys" channel.

    Arguments:
        ctx (Context): The context of the command invocation.
    """

    if ctx.channel.name != "api-keys":  # type: ignore
        return

    user_id = ctx.author.id
    api_key = generate_api_key(user_id)

    try:
        await ctx.author.send(f"Your API key is: `{api_key}`")
        await ctx.send(f"{ctx.author.mention} {Messages.apikey_sent}")
    except discord.Forbidden:
        await ctx.send(f"{ctx.author.mention} {Messages.apikey_error}")


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
async def localdocs(ctx: Context) -> None:
    """Sends a link to the documentation about local deployment."""
    await ctx.send(Messages.local_docs)


@bot.command()
async def localtr(ctx: Context) -> None:
    """Sends a link to the local troubleshooting guide."""
    await ctx.send(Messages.local_troubleshoot)


@bot.command()
async def gethelp(ctx: Context) -> None:
    """Sends a link to the Get Help page."""
    await ctx.send(Messages.get_help)


bot.run(DISCORD_TOKEN)  # type: ignore
