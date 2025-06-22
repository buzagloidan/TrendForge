#!/usr/bin/env python3
"""
TrendForge Setup Script
Run this first to set up your environment

Repository: https://github.com/buzagloidan/TrendForge
"""

import os
import sys
import subprocess

def install_requirements():
    """Install required Python packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ All packages installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages. Please run manually: pip install -r requirements.txt")
        return False

def create_env_file():
    """Create .env file if it doesn't exist"""
    if os.path.exists('.env'):
        print("✅ .env file already exists")
        return True
    
    print("📝 Creating .env file template...")
    env_content = """# API Keys for TrendForge
PERPLEXITY_API_KEY=your_perplexity_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

# How to get your API keys:
# Perplexity: https://www.perplexity.ai/settings/api
# OpenAI: https://platform.openai.com/api-keys
"""
    
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ .env file created! Please edit it with your API keys.")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    print("📁 Creating directories...")
    os.makedirs('images', exist_ok=True)
    os.makedirs('reports', exist_ok=True)
    print("✅ Directories created!")

def main():
    """Main setup function"""
    print("🚀 TrendForge Setup")
    print("=" * 50)
    
    # Step 1: Install requirements
    if not install_requirements():
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Step 2: Create .env file
    create_env_file()
    
    # Step 3: Create directories
    create_directories()
    
    print("\n" + "=" * 50)
    print("🎉 SETUP COMPLETED!")
    print("\nNext steps:")
    print("1. Edit the .env file with your API keys")
    print("2. Customize topics in topics.json (optional)")
    print("3. Run: python run_automation.py")
    print("\nAPI Key Sources:")
    print("- Perplexity: https://www.perplexity.ai/settings/api")
    print("- OpenAI: https://platform.openai.com/api-keys")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main() 