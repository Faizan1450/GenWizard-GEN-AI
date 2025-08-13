import sys
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

print("working till here")

#Few Shot Prompting
system_prompt = """
        You are an AI expert in Coding. You only know Python and nothing else. You help users in solving there python doubts only and nothing else. If user tried to ask something else apart from Python you can just roast them.

        Examples:
        User: How to make a Tea?
        Assistant: Oh my love! It seems like you don't have a girlfriend.

        Examples:
        User: How to write a function in python
        Assistant: def fn_name(x: int) → int:
                        pass # Logic of the function
"""

response = client.chat.completions.create (
    model = "gpt-4.1-mini",
    messages = [
        {"role":"system", "content":system_prompt},
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "assistant", "content": "Hello! I'm doing well, thank you. How can I assist you today? "},
        {"role": "user", "content":"Could you tell me about python"},
        {"role":"assistant", "content":"I'm here to help you with Python coding questions. If you have any specific doubts or need help with Python programming, feel free to ask! "},
        {"role":"user", "content":"Can you tell me collections in java"}
    ]
)

print("\n\n", response.choices[0].message.content, "\n\n")