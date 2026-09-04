import os
import xai_sdk
from xai_sdk.chat import user

client = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"))

chat = client.chat.create(model="grok-2-latest")
chat.append(user("What is the meaning of life?"))

response = chat.sample()
print(response.content)
