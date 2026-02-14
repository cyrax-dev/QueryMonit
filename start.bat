@echo off
chcp 65001 > nul

echo Install UV...
echo ---------------------------------
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
cls

echo Add PATH...
echo ---------------------------------
set Path=C:\Users\%USERNAME%\.local\bin;%Path%
cls

echo Starting...
rmdir /s /q .venv
uv run python -B src/main.py
pause
