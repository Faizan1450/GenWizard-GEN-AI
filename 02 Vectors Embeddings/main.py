from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()
text = "Hello I am Syed Faizan Ali"

result = client.models.embed_content(
            model="gemini-embedding-001",
            contents=text
        )

print("Length of Output", len(result.embeddings[0].values))
print("Vector Embeddings", result.embeddings[0].values)