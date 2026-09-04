import os
import time
import xai_sdk
from xai_sdk.proto import deferred_pb2

client = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"))

# Manual polling (alternative to generate() which does this automatically)
start = client.video.start(
    prompt="A cat lounging in a sunbeam",
    model="grok-imagine-video-1.5",
)

while True:
    result = client.video.get(start.request_id)
    if result.status == deferred_pb2.DeferredStatus.DONE:
        print(result.response.video.url)
        break
    elif result.status == deferred_pb2.DeferredStatus.FAILED:
        print("Generation failed")
        break
    time.sleep(5)
