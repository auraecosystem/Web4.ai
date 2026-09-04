import os
import xai_sdk

client = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"))

info = client.auth.get_api_key_info()
print(f"API Key ID: {info.api_key_id}")
print(f"Team ID: {info.team_id}")
