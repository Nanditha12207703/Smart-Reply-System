from datasets import load_dataset
import json

dataset = load_dataset("daily_dialog", trust_remote_code=True)


pairs = []

# Only use train split for now
for dialog in dataset["train"]:
    utterances = dialog["dialog"]
    for i in range(len(utterances) - 1):
        msg = utterances[i]
        reply = utterances[i+1]
        pairs.append({"message": msg, "replies": [reply]})

# Save top 1000 pairs
with open("dataset.json", "w") as f:
    json.dump(pairs[:1000], f, indent=2)

print("✅ dataset.json with 1000 pairs created!")
