#!/usr/bin/env python3
"""
TrendForge Quick Setup
Helps users configure topics and get started quickly

Repository: https://github.com/buzagloidan/TrendForge
"""

import json
import os

def create_template_config():
    """Create a template configuration"""
    templates = {
        "1": {
            "name": "Technology",
            "content_focus": "Technology and Innovation",
            "topics": [
                "Artificial Intelligence and Machine Learning",
                "Blockchain and Web3 developments",
                "Cybersecurity trends",
                "Cloud computing innovations",
                "Software development trends",
                "Tech startup funding"
            ]
        },
        "2": {
            "name": "Digital Marketing",
            "content_focus": "Digital Marketing and Growth",
            "topics": [
                "Social media marketing trends",
                "Content marketing strategies",
                "Email marketing automation",
                "SEO trends",
                "Influencer marketing",
                "Marketing technology"
            ]
        },
        "3": {
            "name": "Business",
            "content_focus": "Business and Entrepreneurship",
            "topics": [
                "Startup ecosystem",
                "Remote work trends",
                "Leadership strategies",
                "Business automation",
                "E-commerce innovations",
                "Investment trends"
            ]
        }
    }
    
    print("🚀 TrendForge Quick Setup")
    print("=" * 50)
    print("\nChoose a template or create custom:")
    print("1. Technology and Innovation")
    print("2. Digital Marketing")
    print("3. Business and Entrepreneurship")
    print("4. Custom setup")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice in templates:
        template = templates[choice]
        config = {
            "content_focus": template["content_focus"],
            "topics": template["topics"],
            "post_settings": {
                "word_count_range": "300-500",
                "include_hashtags": True,
                "include_questions": True,
                "tone": "professional but engaging"
            }
        }
        print(f"\n✅ Selected: {template['name']}")
    else:
        # Custom setup
        print("\n🛠️ Custom Setup")
        content_focus = input("Enter your content focus: ").strip() or "General Topics"
        
        topics = []
        print("\nAdd topics (press Enter on empty line to finish):")
        while True:
            topic = input(f"Topic {len(topics) + 1}: ").strip()
            if not topic:
                break
            topics.append(topic)
        
        config = {
            "content_focus": content_focus,
            "topics": topics or ["General trends", "Industry updates"],
            "post_settings": {
                "word_count_range": "300-500",
                "include_hashtags": True,
                "include_questions": True,
                "tone": "professional but engaging"
            }
        }
    
    # Save configuration
    with open('topics.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"\n✅ Configuration saved to topics.json")
    print(f"📋 Content Focus: {config['content_focus']}")
    print(f"📊 Topics: {len(config['topics'])}")
    print("\nNext: Configure API keys in .env file and run the automation!")

if __name__ == "__main__":
    create_template_config() 