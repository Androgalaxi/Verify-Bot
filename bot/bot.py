import discord
import os
try:
    from dotenv import load_dotenv
    # Load environment variables from a .env file
    load_dotenv()
    print("dotenv is loaded successfully.")
except ImportError:
    print("python-dotenv is not installed. Skipping dotenv setup.")
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="&", intents=intents)

SERVER_ID = os.getenv("SERVER_ID") or "1234567890" #REPLACE ID's IN .env AND HERE, THIS IS ALL YOU NEED THOUGH.
CHANNEL_ID = os.getenv("CHANNEL_ID") or "1234567890"
ROLE_ID = os.getenv("ROLE_ID") or "1234567890"

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.guild and message.guild.id == SERVER_ID and message.channel.id == CHANNEL_ID:
        if message.content.lower() == "cherry": # Change "cherry" to any word or phrase you prefer
            role = message.guild.get_role(ROLE_ID)
            if role:
                if role not in message.author.roles:
                    await message.author.add_roles(role)
                    await message.channel.send(
                        f"{message.author.mention}, you have been given the role!", delete_after=5 # You can change the delay until the message is deleted
                    )
                else:
                    await message.channel.send(
                        f"{message.author.mention}, you already have the role.", delete_after=5 # You can change the delay until the message is deleted
                    )
            else:
                print(f"Role with ID '{ROLE_ID}' not found in the server.")
        await message.delete()

bot.run(os.getenv("BOT_TOKEN") or "BOT_TOKEN") # REPLACE `or "BOT_TOKEN"` with `or token` if you have a token variable, or with your actual token string within quotations
