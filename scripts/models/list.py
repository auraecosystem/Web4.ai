import os
import xai_sdk

client = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"))

# List language models
for model in client.models.list_language_models():
    print(f"{model.name} (aliases: {', '.join(model.aliases)})")

# List image generation models
for model in client.models.list_image_generation_models():
    print(f"{model.name}")
