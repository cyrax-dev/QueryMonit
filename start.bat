@echo off
chcp 65001 > nul
title Monitoring Bot

echo Install UV...
echo ---------------------------------
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
cls

echo Add PATH...
echo ---------------------------------
set Path=C:\Users\%USERNAME%\.local\bin;%Path%
cls

echo Starting...
uv run src/main.py
pause
