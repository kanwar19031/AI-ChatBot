# 🤖 AI-Powered Educational Chatbot

A versatile chatbot that comes pre-configured with Utkarsh Classes knowledge and can be customized for any website. Built with Streamlit and Google's Gemini Pro AI.

## ✨ Features

- **Dual Mode Operation**
  - Default Utkarsh Classes mode with educational expertise
  - Custom website mode for personalized knowledge bases
- **Interactive Chat Interface**
  - Real-time responses
  - Chat history management
  - Clear and intuitive UI
- **Easy Website Integration**
  - Simple URL input
  - Automatic content extraction
  - Dynamic context switching

## 🚀 Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/kanwar19031/AI-ChatBot
   cd AI-ChatBot
   ```

2. **Set Up Environment**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   python setup.py
   ```

4. **Get Your API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create or sign in to your Google account
   - Click "Create API Key"
   - Copy your new API key

5. **Configure API Key**
   - Create a `.env` file in the project root
   - Add your API key:
     ```text
     GOOGLE_API_KEY=your_api_key_here
     ```

6. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## 💡 Usage

### Utkarsh Classes Mode
- Default mode with pre-loaded educational content
- Perfect for students seeking information about courses and programs
- Just start chatting!

### Custom Website Mode
1. Select "Custom Website" in the sidebar
2. Enter any website URL
3. Click "Create Custom Chatbot"
4. Chat with AI about that website's content

## 🛠️ Technical Details

- **Framework**: Streamlit
- **AI Model**: Google Gemini Pro
- **Web Scraping**: BeautifulSoup4
- **Language**: Python 3.8+

## 📝 Important Notes

- Keep your API key confidential
- The custom website mode works best with text-heavy pages
- Response quality depends on the content quality of the source website

## 🤝 Contributing

Feel free to:
- Open issues
- Submit pull requests
- Suggest improvements
- Report bugs

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Utkarsh Classes & Edutech Pvt Ltd for the educational content
- Google for the Gemini Pro API
- The Streamlit team for their amazing framework

---
Made with ❤️ for education

 
