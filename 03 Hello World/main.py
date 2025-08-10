from openai import OpenAi
load_dotenv()

client = OpenAi()

response = client.models.generate_content (
    model = "gemini-2.0-flash-lite",
    contents=[{
        "role": "user",
        "parts": [
            {"text": "Hello, how are you!!"}
        ]
    }]
    # contents="Explain how AI works in a few words"
)


print("\n\n", response.text, "\n\n")