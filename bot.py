import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.message_content = True

SERVER_ID = 979895174937341972 #Replace with your server ID
CHANNEL_ID = 1367151670730948638 #Replace with your channel ID
ROLE_ID = 979934762166804521  # Replace with your role ID

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.guild and message.guild.id == SERVER_ID and message.channel.id == CHANNEL_ID:
        if message.content.lower() == "voice":
            role = message.guild.get_role(ROLE_ID)
            if role:
                if role not in message.author.roles:
                    await message.author.add_roles(role)
                    await message.channel.send(
                        f"{message.author.mention}, you have been given the Members role!", delete_after=5
                    )
                else:
                    await message.channel.send(
                        f"{message.author.mention}, you already have the Members role.", delete_after=5
                    )
            else:
                print(f"Role with ID '{ROLE_ID}' not found in the server.")
        else:
            error_msg = await message.channel.send(
                f"{message.author.mention}, you have typed the incorrect word. Please re-read the message above and try again.", #Change the text if you'd like
                delete_after=5 #Adjust time as needed
            )
        await message.delete()

bot.run("BOT_TOKEN") #Replace BOT_TOKEN with your own token
