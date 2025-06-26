import streamlit as st
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load dataset
with open("dataset.json", "r", encoding="utf-8") as f:
    dataset = json.load(f)

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Prepare message embeddings
messages = [item["message"] for item in dataset]
message_embeddings = model.encode(messages)

# Smart reply function
def get_smart_replies(user_input, top_k=3):
    input_embedding = model.encode([user_input])
    similarities = cosine_similarity(input_embedding, message_embeddings)
    top_indices = np.argsort(similarities[0])[::-1][:top_k]

    reply_pool = []
    for idx in top_indices:
        reply_pool.extend(dataset[idx]["replies"])

    return list(set(reply_pool))[:5]  # Return top 5 unique replies

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Smart Reply Generator", layout="centered")

st.title("💬 Smart Reply Generator")
st.write("Type a message and get suggested replies based on past conversations.")

user_input = st.text_input("Your Message", placeholder="e.g., Can we reschedule our meeting?")

if st.button("Generate Smart Replies"):
    if user_input.strip() == "":
        st.warning("Please enter a message to get replies.")
    else:
        replies = get_smart_replies(user_input)
        st.subheader("🧠 Suggested Replies:")
        for reply in replies:
            st.markdown(f"- {reply}")
