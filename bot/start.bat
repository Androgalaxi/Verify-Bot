@echo off
title Discord Bot - Always Online
echo Starting the bot...
:loop
python bot.py
echo Bot has stopped. Restarting in 60 seconds...
timeout /t 60 >nul
goto loop
