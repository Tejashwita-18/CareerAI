from src.ai.gemini_client import GeminiClient

client = GeminiClient()

response = client.generate_feedback(
    "Say hello in one sentence."
)

print(response)
