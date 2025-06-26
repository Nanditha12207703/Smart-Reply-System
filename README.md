# 💬 Smart Reply System – Gen AI Project (Retrieval-Based)

## 🔍 Project Overview

This project presents a **Smart Reply System** built using Python and **Sentence Transformers**, with a **Streamlit web interface**. It mimics the functionality of chat assistants by suggesting relevant, pre-written responses based on a user's input. The system uses a retrieval-based approach and is ideal for building conversational interfaces, customer support bots, or productivity assistants.

---

## 💡 Key Features

- ✅ **Semantic Search with Sentence Embeddings**: Finds the most relevant replies using cosine similarity
- 📥 **Top-k Smart Suggestions**: Dynamically returns the top 3–5 most suitable replies
- 📂 **Customizable Dataset**: Built from the `daily_dialog` corpus + manually added domain-specific examples
- 🌐 **Interactive Streamlit App**: Clean, user-friendly interface for testing and showcasing the system

---

## 🧠 How It Works

1. User types a message (e.g., *"Can we reschedule the meeting?"*)
2. The system embeds the message using a Sentence Transformer (`all-MiniLM-L6-v2`)
3. It compares this with the message embeddings from the dataset
4. Retrieves replies from the top-matching messages based on cosine similarity
5. Returns them as smart suggestions

---

## 🛠️ Tools & Technologies Used

- **Python**
- **Sentence Transformers** (Hugging Face)
- **Scikit-learn** (Cosine Similarity)
- **Streamlit** (Web App)
- **Hugging Face Datasets** (`daily_dialog`)

---

## 🖼️ Project Structure

SmartReplyProject/
├── dataset.json # Final message–reply pairs
├── generate_dataset.py # Optional script to build dataset from Hugging Face
├── reply_model.py # Core logic: embeddings + retrieval
└── app.py # Streamlit web app

## 📦 Example Usage

> **User Input:**  
> `"Can we reschedule our meeting?"`

> **Smart Replies:**  
> - Sure, let me know a better time.  
> - No problem, what time works for you?  
> - Yes, happy to reschedule.

---

## 📁 Files Included

- `dataset.json` – Cleaned and enhanced training data  
- `app.py` – Frontend UI with Streamlit  
- `reply_model.py` – Embedding and retrieval logic  
- `generate_dataset.py` – Dataset builder (Hugging Face)  
- `README.md` – Project documentation  
- `screenshot.png` – UI preview (optional)

---

## ⚠️ Notes

> This project is designed for educational and portfolio purposes. It uses open-source models and a publicly available dataset (`daily_dialog`).  
> You can expand it with your own message–reply pairs to suit specific domains like HR chatbots, customer support, or productivity tools.

---

## 📬 Let’s Connect!

I'm always excited to collaborate on AI/ML and NLP-based projects!

- 🔗 **LinkedIn**: [linkedin.com/in/gootynanditha](https://linkedin.com/in/gootynanditha)

---

## 🔖 Tags

`Smart Reply` `GenAI` `Retrieval-based NLP` `Sentence Transformers` `Streamlit` `AI Chatbot` `NLP Capstone` `Portfolio Project`
