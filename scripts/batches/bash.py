import os
import xai_sdk

client = xai_sdk.Client(api_key=os.getenv("XAI_API_KEY"))

# List all batches
batches = client.batch.list(limit=10)
for b in batches.batches:
    print(f"{b.name}: {b.batch_id}")

# Get results for a specific batch
results = client.batch.list_batch_results("BATCH_ID")
for r in results.results:
    print(f"{r.batch_request_id}: {r.response}")
