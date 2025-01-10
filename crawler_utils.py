import requests
from bs4 import BeautifulSoup

def get_website_content(url):
    try:
        # Add headers to mimic a browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Get the webpage content
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
        
        # Get text content
        text = soup.get_text(separator='\n', strip=True)
        
        # Clean up the text
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        text = '\n\n'.join(lines)
        
        return text
        
    except Exception as e:
        return f"Error extracting content: {str(e)}"

def create_context_from_markdown(content):
    return f"""You are an enthusiastic and knowledgeable chat assistant for the website content provided. 
    Use this information as your knowledge base: {content}
    
    Please follow these guidelines:
    1. Be friendly and professional in your responses
    2. If you're not sure about something, say so rather than making up information
    3. Keep responses concise but informative
    4. Use bullet points when listing multiple items
    5. Only use information from the provided content
    """ 