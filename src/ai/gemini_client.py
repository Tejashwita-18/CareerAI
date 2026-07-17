import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

class GeminiClient:
    """
    Client for interacting with Google's Gemini model.
    """

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in .env"
            )
        
        self.client = genai.Client(api_key=api_key)

    def generate_feedback(self, prompt: str) -> str:
        """
        Send prompt to Gemini and return the response.
        """

        print("GeminiClient is running...")
        print("Using model: models/gemini-3.5-flash")

        response = self.client.models.generate_content(
            model = "models/gemini-3.5-flash",
            contents = prompt
        )

        return response.text
