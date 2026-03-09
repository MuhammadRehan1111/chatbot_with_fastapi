import google.genai as genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

model = "gemini-2.0-flash-lite"


def generate_reply(prompt: str):
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        if not response.text:
            raise Exception("Empty response from AI")

        return response.text

    except Exception as e:
        raise Exception(f"AI API Error: {str(e)}")

