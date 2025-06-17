#!/usr/bin/env python3
"""
TrendForge Launcher
Just double-click this file or run: python run_automation.py

Repository: https://github.com/buzagloidan/TrendForge
"""

import sys
import os
from pathlib import Path

def check_requirements():
    """Check if all requirements are met"""
    try:
        import requests
        import openai
        from dotenv import load_dotenv
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_env_file():
    """Check if .env file exists and has required keys"""
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("Please create a .env file with your API keys:")
        print("PERPLEXITY_API_KEY=your_key_here")
        print("OPENAI_API_KEY=your_key_here")
        return False
    
    from dotenv import load_dotenv
    load_dotenv()
    
    perplexity_key = os.getenv('PERPLEXITY_API_KEY')
    openai_key = os.getenv('OPENAI_API_KEY')
    
    if not perplexity_key or perplexity_key == 'your_perplexity_api_key_here':
        print("❌ PERPLEXITY_API_KEY not configured in .env file")
        return False
    
    if not openai_key or openai_key == 'your_openai_api_key_here':
        print("❌ OPENAI_API_KEY not configured in .env file")
        return False
    
    print("✅ API keys are configured")
    return True

def main():
    """Main launcher function"""
    print("🚀 TrendForge Launcher")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Check .env file
    if not check_env_file():
        input("Press Enter to exit...")
        sys.exit(1)
    
    # All checks passed, run the automation
    print("\n🚀 Starting content automation...")
    print("This will take several minutes to complete.\n")
    
    try:
        from content_automation import ContentAutomation
        automation = ContentAutomation()
        automation.run_automation()
        
        print("\n" + "=" * 50)
        print("🎉 AUTOMATION COMPLETED SUCCESSFULLY!")
        print("📄 Check the reports/ folder for your content")
        print("🖼️ Images are saved in the images/ folder")
        
    except Exception as e:
        print(f"\n❌ Error running automation: {e}")
        print("Please check your API keys and internet connection")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main() 