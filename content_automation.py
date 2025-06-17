#!/usr/bin/env python3
"""
TrendForge - AI-Powered Content Automation
Scrapes latest trends using Perplexity API and generates professional LinkedIn posts with AI images
Works with any content domain - topics are configurable via topics.json

Repository: https://github.com/buzagloidan/TrendForge
License: MIT
"""

import os
import requests
import json
import base64
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any
from dotenv import load_dotenv
from openai import OpenAI
import time
from topic_selector import TopicSelector

# Load environment variables
load_dotenv()

class ContentAutomation:
    def __init__(self, config_file: str = "topics.json"):
        self.perplexity_api_key = os.getenv('PERPLEXITY_API_KEY')
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        
        if not self.perplexity_api_key:
            raise ValueError("PERPLEXITY_API_KEY not found in .env file")
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")
            
        self.openai_client = OpenAI(api_key=self.openai_api_key)
        self.perplexity_url = "https://api.perplexity.ai/chat/completions"
        
        # Load configuration
        self.topic_selector = TopicSelector(config_file)
        self.config = self.topic_selector.get_config()
        self.content_focus = self.config.get('content_focus', 'General Topics')
        self.topics = []  # Will be set during topic selection
        
        self.scraped_data = []
        self.generated_posts = []
    
    def set_topics(self, topics: List[str]):
        """Set the topics to be processed"""
        self.topics = topics
    
    def scrape_latest_trends(self, topic: str) -> Dict[str, Any]:
        """Scrape latest trends for a specific topic using Perplexity API"""
        print(f"🔍 Researching latest trends in: {topic}")
        
        # Get current date for recent content filtering
        current_date = datetime.now()
        last_month = current_date - timedelta(days=30)
        
        prompt = f"""
        Search for the LATEST news, trends, and developments in {topic} from the past 30 days only. 
        Focus on:
        - Recent announcements, breakthroughs, or innovations
        - New research findings or studies
        - Industry updates or changes
        - Market analysis or reports
        - Expert opinions and thought leadership
        - Startup developments or funding news
        
        Please provide:
        1. 3-5 most significant recent developments
        2. Key statistics or data points
        3. Notable companies, people, or organizations involved
        4. Future implications or trends
        
        Only include information from {last_month.strftime('%B %Y')} onwards. Ignore older content.
        Content focus area: {self.content_focus}
        """
        
        headers = {
            "Authorization": f"Bearer {self.perplexity_api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "sonar-pro",
            "messages": [
                {
                    "role": "system",
                    "content": f"You are an expert researcher focused on {self.content_focus}. Focus only on the most recent and credible information from the past month."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 1500,
            "temperature": 0.2,
            "top_p": 0.9,
            "return_citations": True,
            "search_domain_filter": ["techcrunch.com", "forbes.com", "wired.com", "reuters.com", "bloomberg.com"]
        }
        
        try:
            response = requests.post(self.perplexity_url, json=payload, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            content = data['choices'][0]['message']['content']
            citations = data.get('citations', [])
            
            return {
                'topic': topic,
                'content': content,
                'citations': citations,
                'timestamp': datetime.now().isoformat()
            }
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error scraping {topic}: {e}")
            return {
                'topic': topic,
                'content': f"Error retrieving data for {topic}",
                'citations': [],
                'timestamp': datetime.now().isoformat()
            }
    
    def generate_linkedin_post(self, trend_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a LinkedIn post based on scraped trend data"""
        print(f"✍️ Generating LinkedIn post for: {trend_data['topic']}")
        
        post_settings = self.config.get('post_settings', {})
        word_count = post_settings.get('word_count_range', '300-500')
        tone = post_settings.get('tone', 'professional but engaging')
        include_hashtags = post_settings.get('include_hashtags', True)
        include_questions = post_settings.get('include_questions', True)
        
        prompt = f"""
        Based on this latest research about {trend_data['topic']}:
        
        {trend_data['content']}
        
        Create a professional LinkedIn post ({word_count} words) that:
        
        1. Starts with a compelling hook about the latest development
        2. Explains why this trend matters to professionals in {self.content_focus}
        3. Includes specific data points or examples from the research
        4. Discusses implications for the future
        {'5. Ends with a thought-provoking question to encourage engagement' if include_questions else '5. Ends with a strong call-to-action or insight'}
        6. Uses {tone} language
        {'7. Includes 3-5 relevant hashtags' if include_hashtags else '7. No hashtags needed'}
        
        Format: Write as a cohesive LinkedIn post, not bullet points. Make it engaging and shareable.
        """
        
        try:
            response = self.openai_client.chat.completions.create(
                model="o3",
                messages=[
                    {
                        "role": "system",
                        "content": f"You are a content strategist who creates engaging LinkedIn posts for professionals in {self.content_focus}. Write in a {tone} tone."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=800
            )
            
            post_content = response.choices[0].message.content
            
            return {
                'topic': trend_data['topic'],
                'post_content': post_content,
                'source_data': trend_data['content'],
                'citations': trend_data['citations'],
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"❌ Error generating post for {trend_data['topic']}: {e}")
            return {
                'topic': trend_data['topic'],
                'post_content': f"Error generating post for {trend_data['topic']}",
                'source_data': trend_data['content'],
                'citations': trend_data['citations'],
                'timestamp': datetime.now().isoformat()
            }
    
    def generate_post_image(self, post_data: Dict[str, Any]) -> str:
        """Generate an image for the LinkedIn post using image-gen-1"""
        print(f"🎨 Generating image for: {post_data['topic']}")
        
        # Generate unique timestamp for this session
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Create varied image prompt to ensure uniqueness
        style_variations = [
            "Modern minimalist design with geometric shapes",
            "Contemporary business illustration with clean lines", 
            "Professional infographic style with data elements",
            "Sleek corporate design with abstract elements",
            "Modern flat design with bold color accents"
        ]
        
        # Use random selection for style variation to ensure uniqueness
        selected_style = random.choice(style_variations)
        
        # Add random color emphasis for additional uniqueness
        color_emphasis = random.choice([
            "with vibrant blue accents",
            "with subtle green highlights", 
            "with modern purple tones",
            "with professional teal elements",
            "with clean orange details"
        ])
        
        # Create image prompt based on the post content
        image_prompt = f"""
        Create a unique professional image for a LinkedIn post about {post_data['topic']} in the context of {self.content_focus}. 
        The image should be:
        - Clean and professional business/tech aesthetic
        - Include subtle relevant elements (digital interfaces, charts, modern icons)
        - Use a modern color palette (blues, greens, grays, whites)
        - Suitable for LinkedIn sharing
        - High quality and visually appealing
        - No text overlay needed
        - Generated at {timestamp} with unique styling
        
        Style: {selected_style} {color_emphasis}, ensuring this is a completely fresh and unique image
        """
        
        try:
            response = self.openai_client.images.generate(
                model="image-gen-1",
                prompt=image_prompt,
                size="1024x1024",
                n=1
            )
            
            # Get image URL and download
            image_url = response.data[0].url
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            
            # Create images directory if it doesn't exist
            os.makedirs('images', exist_ok=True)
            
            # Save image with topic name and timestamp for uniqueness
            safe_topic = "".join(c for c in post_data['topic'] if c.isalnum() or c in (' ', '-', '_')).rstrip()
            unique_timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]  # Include microseconds for uniqueness
            image_filename = f"images/{safe_topic.replace(' ', '_').lower()}_{unique_timestamp}.png"
            
            with open(image_filename, 'wb') as f:
                f.write(image_response.content)
            
            return image_filename
            
        except Exception as e:
            print(f"❌ Error generating image for {post_data['topic']}: {e}")
            return ""
    
    def run_automation(self, interactive_mode: bool = True):
        """Run the complete automation process"""
        print("🚀 Starting TrendForge Content Automation...")
        print(f"📋 Content Focus: {self.content_focus}")
        
        # Topic selection
        if interactive_mode:
            print("\n" + "="*50)
            print("TOPIC SELECTION")
            print("="*50)
            self.topics = self.topic_selector.interactive_selection()
        else:
            self.topics = self.config['topics']
        
        print(f"\n📅 Researching trends from the past 30 days")
        print(f"📊 Topics to research: {len(self.topics)}")
        
        # Step 1: Scrape latest trends for all topics
        print("\n" + "="*50)
        print("STEP 1: SCRAPING LATEST TRENDS")
        print("="*50)
        
        for i, topic in enumerate(self.topics, 1):
            print(f"\n[{i}/{len(self.topics)}] Processing: {topic}")
            trend_data = self.scrape_latest_trends(topic)
            self.scraped_data.append(trend_data)
            
            # Add delay to respect API rate limits
            time.sleep(2)
        
        print(f"\n✅ Completed scraping {len(self.scraped_data)} topics")
        
        # Step 2: Generate LinkedIn posts for top trends
        print("\n" + "="*50)
        print("STEP 2: GENERATING LINKEDIN POSTS")
        print("="*50)
        
        # Select top 5-8 most promising topics based on content quality
        quality_topics = [data for data in self.scraped_data if len(data['content']) > 200 and 'Error' not in data['content']]
        selected_topics = quality_topics[:8]  # Take top 8 topics
        
        for i, trend_data in enumerate(selected_topics, 1):
            print(f"\n[{i}/{len(selected_topics)}] Generating post for: {trend_data['topic']}")
            post_data = self.generate_linkedin_post(trend_data)
            
            # Generate image for the post
            image_path = self.generate_post_image(post_data)
            post_data['image_path'] = image_path
            
            self.generated_posts.append(post_data)
            
            # Add delay between OpenAI calls
            time.sleep(1)
        
        print(f"\n✅ Generated {len(self.generated_posts)} LinkedIn posts with images")
        
        # Step 3: Save to HTML file
        report_file = self.save_to_html()
        
        print("\n🎉 Automation completed successfully!")
        print(f"📄 Results saved to: {report_file}")
        print(f"🖼️ Images saved to: images/ directory")
    
    def save_to_html(self):
        """Save all generated content to an HTML file for review"""
        print("\n📄 Generating HTML report...")
        
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Content Automation Report - {self.content_focus}</title>
            <style>
                body {{ 
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                    margin: 0; 
                    padding: 20px; 
                    background-color: #f8f9fa; 
                    line-height: 1.6; 
                }}
                .container {{ 
                    max-width: 1200px; 
                    margin: 0 auto; 
                    background: white; 
                    padding: 30px; 
                    border-radius: 10px; 
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
                }}
                .header {{ 
                    text-align: center; 
                    margin-bottom: 40px; 
                    padding-bottom: 20px; 
                    border-bottom: 2px solid #007acc; 
                }}
                .header h1 {{ 
                    color: #007acc; 
                    margin-bottom: 10px; 
                }}
                .content-focus {{ 
                    background: #e8f4fd; 
                    padding: 15px; 
                    border-radius: 8px; 
                    margin-bottom: 30px; 
                    text-align: center; 
                    font-size: 1.1em; 
                    color: #0066cc; 
                }}
                .stats {{ 
                    display: flex; 
                    justify-content: space-around; 
                    margin-bottom: 40px; 
                    padding: 20px; 
                    background: #f8f9fa; 
                    border-radius: 8px; 
                }}
                .stat-item {{ 
                    text-align: center; 
                }}
                .stat-number {{ 
                    font-size: 2em; 
                    font-weight: bold; 
                    color: #007acc; 
                }}
                .post-card {{ 
                    margin-bottom: 40px; 
                    padding: 25px; 
                    border: 1px solid #e0e0e0; 
                    border-radius: 8px; 
                    background: #ffffff; 
                    box-shadow: 0 2px 4px rgba(0,0,0,0.05); 
                }}
                .post-header {{ 
                    background: linear-gradient(135deg, #007acc, #0066cc); 
                    color: white; 
                    padding: 15px; 
                    border-radius: 8px 8px 0 0; 
                    margin: -25px -25px 20px -25px; 
                }}
                .post-title {{ 
                    margin: 0; 
                    font-size: 1.3em; 
                }}
                .post-content {{ 
                    background: #f8f9fa; 
                    padding: 20px; 
                    border-radius: 6px; 
                    margin: 20px 0; 
                    white-space: pre-wrap; 
                    font-size: 1.1em; 
                    line-height: 1.7; 
                }}
                .post-image {{ 
                    text-align: center; 
                    margin: 20px 0; 
                }}
                .post-image img {{ 
                    max-width: 400px; 
                    border-radius: 8px; 
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
                }}
                .citations {{ 
                    margin-top: 20px; 
                    padding: 15px; 
                    background: #fff3cd; 
                    border-radius: 6px; 
                    border-left: 4px solid #ffc107; 
                }}
                .timestamp {{ 
                    color: #6c757d; 
                    font-size: 0.9em; 
                    text-align: right; 
                    margin-top: 15px; 
                }}
                .footer {{ 
                    text-align: center; 
                    margin-top: 40px; 
                    padding-top: 20px; 
                    border-top: 1px solid #e0e0e0; 
                    color: #6c757d; 
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🚀 Content Automation Report</h1>
                    <p>Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
                </div>
                
                <div class="content-focus">
                    <strong>Content Focus:</strong> {self.content_focus}
                </div>
                
                <div class="stats">
                    <div class="stat-item">
                        <div class="stat-number">{len(self.topics)}</div>
                        <div>Topics Researched</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number">{len(self.generated_posts)}</div>
                        <div>Posts Generated</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number">{len([p for p in self.generated_posts if p.get('image_path')])}</div>
                        <div>Images Created</div>
                    </div>
                </div>
        """
        
        # Add each generated post
        for i, post in enumerate(self.generated_posts, 1):
            # Fix image path to be relative from reports/ folder
            image_path = ""
            if post.get('image_path'):
                # Convert images/filename.png to ../images/filename.png for reports folder
                image_path = f"../{post['image_path']}"
            
            html_content += f"""
                <div class="post-card">
                    <div class="post-header">
                        <h2 class="post-title">#{i}: {post['topic']}</h2>
                    </div>
                    
                    <div class="post-content">{post['post_content']}</div>
                    
                    {f'<div class="post-image"><img src="{image_path}" alt="Generated image for {post["topic"]}" /></div>' if image_path else ''}
                    
                    {f'<div class="citations"><strong>Sources:</strong><br>{"<br>".join(post["citations"][:3]) if post["citations"] else "Real-time web research"}</div>' if post.get('citations') else ''}
                    
                    <div class="timestamp">Generated: {post['timestamp']}</div>
                </div>
            """
        
        html_content += f"""
                <div class="footer">
                    <p>🤖 Generated by TrendForge</p>
                    <p>Powered by Perplexity Sonar-Pro + ChatGPT o3 + image-gen-1</p>
                    <p>Content Focus: {self.content_focus}</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Create reports directory if it doesn't exist
        os.makedirs('reports', exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        safe_focus = "".join(c for c in self.content_focus if c.isalnum() or c in (' ', '-', '_')).rstrip()
        report_filename = f'reports/content_report_{safe_focus.replace(" ", "_").lower()}_{timestamp}.html'
        
        # Save HTML file
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return report_filename


if __name__ == "__main__":
    try:
        automation = ContentAutomation()
        automation.run_automation()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please check your .env file and make sure your API keys are configured correctly.") 