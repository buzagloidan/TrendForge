#!/usr/bin/env python3
"""
Interactive Topic Selector for Content Automation
Allows users to easily select or customize topics without editing code
"""

import json
import os
from typing import List, Dict, Any

class TopicSelector:
    def __init__(self, config_file: str = "topics.json"):
        self.config_file = config_file
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """Load topics configuration from JSON file"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ Config file {self.config_file} not found!")
            return self.create_default_config()
    
    def create_default_config(self) -> Dict[str, Any]:
        """Create a default configuration"""
        default_config = {
            "content_focus": "General Topics",
            "topics": [
                "Technology trends",
                "Business innovation",
                "Digital transformation",
                "Industry insights",
                "Market analysis"
            ],
            "post_settings": {
                "word_count_range": "300-500",
                "include_hashtags": True,
                "include_questions": True,
                "tone": "professional but engaging"
            }
        }
        
        # Save default config
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=2)
        
        print(f"✅ Created default config file: {self.config_file}")
        return default_config
    
    def display_current_topics(self):
        """Display currently configured topics"""
        print(f"\n📋 Current Content Focus: {self.config['content_focus']}")
        print(f"📊 Number of topics: {len(self.config['topics'])}")
        print("\nConfigured Topics:")
        for i, topic in enumerate(self.config['topics'], 1):
            print(f"  {i:2d}. {topic}")
    
    def interactive_selection(self) -> List[str]:
        """Interactive topic selection interface"""
        print("🎯 Content Automation - Topic Selection")
        print("=" * 50)
        
        self.display_current_topics()
        
        while True:
            print("\nOptions:")
            print("1. Use all current topics")
            print("2. Select specific topics")
            print("3. Add new topics")
            print("4. Edit content focus")
            print("5. Save and exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                return self.config['topics']
            
            elif choice == "2":
                return self.select_specific_topics()
            
            elif choice == "3":
                self.add_new_topics()
                self.display_current_topics()
            
            elif choice == "4":
                self.edit_content_focus()
                self.display_current_topics()
            
            elif choice == "5":
                self.save_config()
                return self.config['topics']
            
            else:
                print("❌ Invalid choice. Please try again.")
    
    def select_specific_topics(self) -> List[str]:
        """Allow user to select specific topics from the list"""
        print("\n📝 Select topics by number (comma-separated, e.g., 1,3,5-8):")
        
        selection = input("Your selection: ").strip()
        selected_topics = []
        
        try:
            # Parse selection (supports ranges like 1,3,5-8)
            parts = selection.split(',')
            indices = set()
            
            for part in parts:
                part = part.strip()
                if '-' in part:
                    start, end = map(int, part.split('-'))
                    indices.update(range(start-1, end))
                else:
                    indices.add(int(part) - 1)
            
            # Get selected topics
            for i in sorted(indices):
                if 0 <= i < len(self.config['topics']):
                    selected_topics.append(self.config['topics'][i])
            
            print(f"\n✅ Selected {len(selected_topics)} topics:")
            for topic in selected_topics:
                print(f"  • {topic}")
            
            return selected_topics
            
        except ValueError:
            print("❌ Invalid selection format. Using all topics.")
            return self.config['topics']
    
    def add_new_topics(self):
        """Add new topics to the configuration"""
        print("\n➕ Add New Topics (press Enter on empty line to finish):")
        
        new_topics = []
        while True:
            topic = input("Enter topic: ").strip()
            if not topic:
                break
            new_topics.append(topic)
            print(f"  ✅ Added: {topic}")
        
        if new_topics:
            self.config['topics'].extend(new_topics)
            print(f"\n✅ Added {len(new_topics)} new topics!")
    
    def edit_content_focus(self):
        """Edit the content focus description"""
        current_focus = self.config['content_focus']
        print(f"\n📝 Current content focus: {current_focus}")
        
        new_focus = input("Enter new content focus (or press Enter to keep current): ").strip()
        if new_focus:
            self.config['content_focus'] = new_focus
            print(f"✅ Updated content focus to: {new_focus}")
    
    def save_config(self):
        """Save current configuration to file"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2)
            print(f"✅ Configuration saved to {self.config_file}")
        except Exception as e:
            print(f"❌ Error saving configuration: {e}")
    
    def get_config(self) -> Dict[str, Any]:
        """Return current configuration"""
        return self.config


def main():
    """Main function for standalone execution"""
    selector = TopicSelector()
    selected_topics = selector.interactive_selection()
    
    print(f"\n🎉 Final selection: {len(selected_topics)} topics")
    print("Ready to run content automation!")


if __name__ == "__main__":
    main() 