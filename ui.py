import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="AI Code Copilot", page_icon="🤖", layout="centered")

st.title("🤖 Local AI Code Copilot")
st.write("Ask questions about your codebase using a local RAG-based AI system.")

question = st.text_area(
    "Enter your question:", placeholder="Where is the EmbeddingModel implemented?"
)

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    API_URL, json={"question": question}, timeout=120
                )
                response.raise_for_status()
                answer = response.json().get("answer", "")
                st.success("Answer")
                st.write(answer)
            except Exception as e:
                st.error(f"Error: {e}")
