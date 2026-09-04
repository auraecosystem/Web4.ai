import os
import xai_sdk
from xai_sdk.chat import assistant, system, user

client = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"))

# Option A: compact a Chat in place. Prior messages are replaced with the
# encrypted compaction blob; chat.sample() continues to work transparently.
chat = client.chat.create(model="grok-4.6", use_encrypted_content=True)
chat.append(system("You are a concise and knowledgeable science tutor."))
chat.append(user("What is the Higgs boson and why is it important?"))
chat.append(chat.sample())
# ... many more turns ...

compact = chat.compact()
print(f"Dropped {compact.dropped_message_count} messages, "
      f"summary used {compact.usage.total_tokens} tokens")

# Option B: compact a standalone message list with client.chat.compact_context().
messages = [
    system("You are a concise and knowledgeable science tutor."),
    user("What is the Higgs boson and why is it important?"),
    assistant("The Higgs boson is an elementary particle..."),
]
compact = client.chat.compact_context(model="grok-4.6", messages=messages)

# Hand the compaction to a fresh chat; appending replaces existing messages
# with the encrypted blob.
new_chat = client.chat.create(model="grok-4.6", use_encrypted_content=True)
new_chat.append(compact)
new_chat.append(user("What gives particles their mass?"))
print(new_chat.sample().content)
