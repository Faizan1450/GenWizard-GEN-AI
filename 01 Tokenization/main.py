import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hello I am Syed Faizan Ali"
tokens = enc.encode(text)

print("Tokens: ", tokens)

tokens:  [13225, 357, 939, 25254, 295, 16792, 58544, 23100]
decoded = enc.decode(tokens)
print(decoded)