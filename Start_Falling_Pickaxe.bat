@echo off
title Falling Pickaxe
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\run.ps1"
if errorlevel 1 (
    echo.
    echo Game could not be started.
    echo Check that Python 3.13 is installed and run.ps1 works.
    pause
)
