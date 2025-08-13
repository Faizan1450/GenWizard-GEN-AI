from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

print("working till here")

#Zero Shot Prompting

response = client.chat.completions.create (
    model = "gpt-4.1-nano",
    messages = [
        {"role": "System", "content": "Hello, how are you?"},
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "user", "content": "Hello, how are you?"},
    ]
)

print("\n\n", response.choices[0].message.content, "\n\n")