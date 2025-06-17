#!/bin/bash

echo ""
echo "===================================================="
echo "                🚀 TrendForge"
echo "===================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "❌ Python is not installed or not in PATH"
    echo "Please install Python from https://python.org"
    echo "Press any key to exit..."
    read -n 1
    exit 1
fi

# Determine which python command to use
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

echo "🚀 Starting TrendForge..."
echo ""

# Run the automation
$PYTHON_CMD run_automation.py

echo ""
echo "===================================================="
echo "Process completed. Check the reports folder for results."
echo "===================================================="
echo "Press any key to exit..."
read -n 1 