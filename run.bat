@echo off
title TrendForge
echo.
echo ====================================================
echo                  🚀 TrendForge
echo ====================================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

:: Run the automation
echo 🚀 Starting TrendForge...
echo.
python run_automation.py

echo.
echo ====================================================
echo Process completed. Check the reports folder for results.
echo ====================================================
pause 