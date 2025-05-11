import google.generativeai as genai
from prompts import system_prompt, get_links_user_prompt
from dotenv import load_dotenv
import os
load_dotenv()


api_key = os.getenv('GOOGLE_API_KEY_1')
if api_key:
    print("API Key looks good.")
else:
    print("There might be some problem with your API Key. Please check.")

MODEL = "gemini-2.0-flash-lite"
genai.configure(api_key=api_key)
GEMINI = genai.GenerativeModel(MODEL)
prompt = "Explain how AI works in a few words"
response = GEMINI.generate_content(prompt)
print(response.text)

def create_testcase():
    messages = []

    full_prompt = f"""
    System: {system_prompt()}

    User: {get_links_user_prompt()}

    Please respond in valid Excel format.
    """
    try:
        response = genai.GenerativeModel(MODEL).generate_content(full_prompt)
        raw_text = response.text.strip()

    except Exception as E:
        print("Error decoding response", E)
        return None

    return raw_text