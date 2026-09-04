import os
import xai_sdk

client = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"))

tokens = client.tokenize.tokenize_text(
    text="Hello, world!",
    model="grok-4.6",
)

print(f"Token count: {len(tokens)}")
for token in tokens:
    print(f"  {token.token_id}: {token.string_token!r}")
