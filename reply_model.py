import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load dataset
with open("dataset.json", "r", encoding="utf-8") as f:
    dataset = json.load(f)

# Load sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Extract and embed all messages
messages = [item["message"] for item in dataset]
message_embeddings = model.encode(messages)

# Function to get smart replies
def get_smart_replies(user_input):
    input_embedding = model.encode([user_input])
    similarities = cosine_similarity(input_embedding, message_embeddings)
    
    top_k = 3  # Number of top matches
    top_indices = np.argsort(similarities[0])[::-1][:top_k]

    # Collect replies from top-k messages
    reply_pool = []
    for idx in top_indices:
        reply_pool.extend(dataset[idx]["replies"])

    # Remove duplicates and return
    smart_replies = list(set(reply_pool))
    return smart_replies

# Example use
if __name__ == "__main__":
    user_message = input("Enter your message: ")
    suggestions = get_smart_replies(user_message)
    print("\nSuggested Replies:")
    for reply in suggestions[:3]:
        print(f"- {reply}")
