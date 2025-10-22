import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI()
messages = []

def call_ai():
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=messages
    )
    message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": message})
    print(f"AI: {message}")

while True:
    message = input("Send a message to the LLM...")
    if message == "quit":
        break
    else:
        messages.append({
            "role":"user",
            "content": message
        })
        print(f"User: {message}")
        call_ai()