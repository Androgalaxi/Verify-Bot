@echo off
title Discord Bot - Always Online
echo Starting the bot...
:loop
python (insert your file path to the bot.py file here)
echo Bot has stopped. Restarting in 60 seconds...
timeout /t 60 >nul
goto loop
