# Frak: Your AI Voice Assistant

This simple Python script implements a command-line interface for interacting with Google's Gemini Pro language model. It simulates Frak, an AI voice assistant designed to help users with various tasks such as setting reminders, creating lists, answering questions, summarizing information, and generating creative text formats.

## Prerequisites

* **Python 3.7 or higher:** Ensure you have a compatible Python version installed.
* **Google Cloud Project:** You'll need a Google Cloud project with the Gemini API enabled.
* **Gemini API Key:** Obtain an API key for accessing the Gemini Pro model.
* **`google-generativeai` Library:** Install the necessary library using pip:


`pip install google-generativeai`
Note: You might need a virtual environment if you are running this code on vscode, etc.



# Setup:
**clone the respository:**
`git clone https://github.com/your-username/frak-ai-assistant.git  # Replace with your repo URL
cd frak-ai-assistant`
**Set the API key**
get the API key and set it in this line: `genai.configure(api_key="GEMINI_API_KEY")`
**Test**
Type `python3 main.py` and type your question in the input

