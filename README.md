# Verify-Bot
A simple bot to force users to type a keyword to gain access to your Discord server.

Thanks for viewing this page!

## How to
- Step 1: Start by downloading the [`bot folder`](bot)
- Step 2: Open the [`bot.py`](bot/bot.py) and [`.env`](bot/.env) file in Visual Studio Code
- Step 3: Replace the SERVER_ID, CHANNEL_ID, and ROLE_ID with your server ID, channel ID of choice, and role ID for the role you want members to gain (or do it in the [`.env`](bot/.env))
- Step 4: Open and edit the [`start.bat`](bot/start.bat) file by adding your file path where the [`start.bat`](bot/start.bat) file is located. Once you place your file path save the changes.
- Step 5: Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create your own bot
- Step 6: Grab your bots token and navigate to OAuth2 and select the Discord Provided Link then for Scopes select bot. For bot permissions select Send Messages, View Channels, Manage Roles Manage Messages, and Read Message History.
- Step 7: At the bottom of the [`bot.py`](bot/bot.py) file, edit the part that says `"BOT_TOKEN"` and paste in your bots token (Or edit in the [`.env`](bot/.env))
- Step 8: In the terminal type in either `pip install discord.py` or `python -m pip install discord.py` (assuming you already have Python installed to your system)
- Step 9: Open the [`start.bat`](bot/start.bat) file
- Step 10: Test and ensure the bot works

For any issues submit an issue in the [Issues](https://github.com/Androgalaxi/Verify-Bot/issues) page.

Enjoy!
