# 🚀 TrendForge

> AI-powered content automation that generates professional LinkedIn posts from the latest industry trends using Perplexity and OpenAI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Powered by OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-412991.svg)](https://openai.com/)
[![Powered by Perplexity](https://img.shields.io/badge/Powered%20by-Perplexity-5865F2.svg)](https://perplexity.ai/)

An intelligent content creation system that researches the latest trends using Perplexity API and generates professional LinkedIn posts with AI-generated images. Works with any content domain - completely configurable!

## ✨ Key Features

- **🔧 Fully Configurable**: No more hardcoded topics! Configure your content focus in `topics.json`
- **🎯 Interactive Topic Selection**: Choose which topics to research without editing code
- **📊 Real-time Research**: Scrapes latest trends from the past 30 days using Perplexity's advanced Sonar-Pro model
- **🤖 AI Content Generation**: Creates professional LinkedIn posts (300-500 words) using ChatGPT 4o
- **🎨 Image Creation**: Generates custom images for each post using DALL-E 3
- **📄 Professional Reports**: Timestamped HTML reports with all generated content
- **⚡ One-Click Execution**: Simple `.bat` file for Windows, `.sh` for Mac/Linux

## 🎯 How It Works

1. **📋 Topic Configuration**: Edit `topics.json` or use interactive selection
2. **🔍 Research Phase**: Uses Perplexity API to find latest news and trends
3. **✍️ Content Generation**: ChatGPT 4o transforms research into engaging LinkedIn posts
4. **🎨 Image Creation**: DALL-E 3 generates professional images for each post
5. **📊 Report Generation**: Compiles everything into beautiful HTML reports

## 🛠️ Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

Copy the example environment file and add your API keys:

```bash
cp env.example .env
```

Then edit `.env` with your actual API keys:

```env
PERPLEXITY_API_KEY=your_perplexity_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

**Get your API keys:**
- **Perplexity API**: [perplexity.ai/settings/api](https://perplexity.ai/settings/api)
- **OpenAI API**: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

### 3. Configure Your Topics

#### Option A: Edit the Configuration File
Edit `topics.json` to set your content focus and topics:

```json
{
  "content_focus": "Your Industry/Niche",
  "topics": [
    "Your first topic",
    "Your second topic",
    "etc..."
  ]
}
```

#### Option B: Use Interactive Selection
Run the topic selector to customize on-the-fly:

```bash
python topic_selector.py
```

### 4. Run the Automation

**Windows (One-Click):**
```
Double-click: run.bat
```

**Mac/Linux (One-Click):**
```bash
chmod +x run.sh
./run.sh
```

**Command Line (Any OS):**
```bash
python run_automation.py
```

## 📋 Example Content Focuses

The system works with any content domain. Here are some examples:

### 🚀 Technology
- AI and Machine Learning
- Blockchain and Web3
- Cybersecurity
- Cloud Computing
- DevOps and Software Development

### 💼 Business
- Digital Marketing
- E-commerce
- Fintech
- Startup Ecosystem
- Remote Work

### 🏥 Healthcare
- Digital Health
- Telemedicine
- Health Tech Innovation
- Medical AI
- Wellness Trends

### 🎨 Creative Industries
- Design Trends
- Creative Technology
- Digital Art
- Content Creation
- Brand Innovation

## 📊 Output

The system generates:

1. **📄 HTML Reports**: Professional reports in `reports/` directory
2. **🖼️ Images**: AI-generated images in `images/` directory
3. **📝 LinkedIn Posts**: Ready-to-post content with:
   - Compelling hooks
   - Professional insights
   - Data points and examples
   - Future implications
   - Engagement questions
   - Relevant hashtags

## ⚙️ Advanced Configuration

### Topics Configuration (`topics.json`)

```json
{
  "content_focus": "Your Industry Focus",
  "topics": [
    "List of topics to research"
  ],
  "post_settings": {
    "word_count_range": "300-500",
    "include_hashtags": true,
    "include_questions": true,
    "tone": "professional but engaging"
  }
}
```

### Interactive Topic Selection

The system includes a powerful topic selector:

- **Select All**: Use all configured topics
- **Custom Selection**: Choose specific topics (e.g., "1,3,5-8")
- **Add Topics**: Add new topics on-the-fly
- **Edit Focus**: Change your content focus area

## 🔧 Customization Options

### Post Generation Settings
- **Word Count**: Adjust post length (default: 300-500 words)
- **Tone**: Change writing style (professional, casual, etc.)
- **Hashtags**: Enable/disable hashtag inclusion
- **Questions**: Include/exclude engagement questions

### Research Settings
- **Time Range**: Modify research period (default: 30 days)
- **Source Domains**: Customize trusted news sources
- **Content Quality**: Adjust minimum content length thresholds

## 💰 Cost Estimation

**Per Full Run (8 posts):**
- Perplexity Sonar-Pro: ~$8-12 (advanced model)
- OpenAI API (GPT-4o + DALL-E 3): ~$10-15
- **Total**: ~$18-27 per run

*Costs may vary based on content complexity and API pricing*

## 🚀 Getting Started Examples

### For Tech Bloggers
```json
{
  "content_focus": "Technology and Innovation",
  "topics": ["AI developments", "Startup funding", "Tech policy"]
}
```

### For Marketing Professionals
```json
{
  "content_focus": "Digital Marketing",
  "topics": ["Social media trends", "Marketing automation", "Brand strategy"]
}
```

### For Healthcare Professionals
```json
{
  "content_focus": "Healthcare Innovation",
  "topics": ["Digital health", "Medical AI", "Telemedicine"]
}
```

## 🔒 Rate Limits & Best Practices

- **Automatic Delays**: Built-in delays respect API rate limits
- **Quality Filtering**: Only generates posts from high-quality research
- **Error Handling**: Graceful handling of API errors
- **Retry Logic**: Automatic retries for transient failures

## 🆘 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Check your `.env` file configuration
   - Verify API keys are active and have sufficient credits

2. **No Content Generated**
   - Ensure topics are relevant and have recent developments
   - Check Perplexity API key has search capabilities

3. **Image Generation Fails**
   - Verify OpenAI account has DALL-E 3 access
   - Check OpenAI API usage limits

4. **Empty Research Results**
   - Try broader topic descriptions
   - Verify internet connectivity

## 📝 License

This project is for educational and professional use. Please ensure compliance with API terms of service.

## 🤝 Support

Need help? Check:
1. API key configuration in `.env` file
2. Internet connectivity
3. API service status pages
4. Console output for specific error messages

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### 🔥 Priority Areas
- New content sources (Reddit, Twitter APIs)
- Additional output formats (Twitter, Instagram, Facebook)
- Web interface for non-technical users
- Content scheduling and analytics

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Contributors

Thanks to all contributors who have helped make TrendForge better!

<!-- Add contributor avatars here when available -->

## 📧 Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/buzagloidan/TrendForge/issues)
- **Discussions**: [Join the community discussion](https://github.com/buzagloidan/TrendForge/discussions)

## ⭐ Star History

If you find TrendForge useful, please consider giving it a star! ⭐

---

**Ready to forge amazing content from trends?** 🚀

1. `git clone https://github.com/buzagloidan/TrendForge.git`
2. Configure your topics → Run the automation → Get professional content! 