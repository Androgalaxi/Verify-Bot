import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="&", intents=intents)

SERVER_ID = 1234567890  # Replace with your server ID
CHANNEL_ID = 1234567890  # Replace with your channel ID
ROLE_ID = 1234567890  # Replace with your role ID

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

bot.run("BOT_TOKEN")
