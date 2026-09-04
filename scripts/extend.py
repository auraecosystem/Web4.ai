import os
import xai_sdk

client = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"))

response = client.video.extend(
    prompt="The camera slowly zooms out to reveal the city skyline",
    model="grok-imagine-video-1.5",
    video_url="https://data.x.ai/docs/video-generation/portrait-wave.mp4",
    duration=6,
)

print(response.url)
