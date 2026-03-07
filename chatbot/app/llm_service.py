import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-pro")

def generate_reply(prompt: str):

    try:
        response = model.generate_content(prompt)

        if not response.text:
            raise Exception("Empty response from AI")

        return response.text

    except Exception as e:
        raise Exception(f"AI API Error: {str(e)}")