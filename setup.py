import subprocess
import sys

def setup():
    print("Setting up Utkarsh Classes Chatbot...")
    
    # Install requirements
    print("Installing requirements...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    print("\nSetup complete! You can now run the chatbot with:")
    print("streamlit run app.py")

if __name__ == "__main__":
    setup() 