import os
import xai_sdk
from xai_sdk.chat import user

client = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"))

# Create a batch
batch = client.batch.create("my_batch")
print(f"Batch ID: {batch.batch_id}")

# Add chat requests to the batch
chats = []
for country in ["UK", "USA", "Egypt"]:
    chat = client.chat.create(
        model="grok-4.6",
        batch_request_id=f"capital_{country.lower()}",
    )
    chat.append(user(f"What is the capital of {country}?"))
    chats.append(chat)

client.batch.add(batch.batch_id, chats)
