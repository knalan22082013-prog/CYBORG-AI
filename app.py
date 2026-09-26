import streamlit as st
from google import genai

st.set_page_config(page_title="CYBORG AI", page_icon="🤖")

st.title("🤖 CYBORG AI Assistant")

# Your API key directly in the code
API_KEY = "AQ.AbBRN6KQCzWQYqf_57LA0KXJPgZLxskvBj5gTAQf8qduJ16G."

# Explicitly tell the client to use the developer API key, not Vertex AI
client = genai.Client(api_key=API_KEY, vertexai=False)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask CYBORG something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Error: {e}")
