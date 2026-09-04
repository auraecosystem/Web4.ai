import os
import xai_sdk
from xai_sdk.chat import user

client = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"))

chat = client.chat.create(model="grok-4.6")
chat.append(user("Tell me a short joke"))

for response, chunk in chat.stream():
    print(chunk.content, end="", flush=True)
print()
