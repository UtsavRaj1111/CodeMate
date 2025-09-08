import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Set page config
st.set_page_config(
    page_title="CodeMate - Your Coding Assistant",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for chatbot UI
st.markdown(
    """
    <style>
    /* Full page solid background */
    .stApp {
        background-color: #1e1e2f !important;
        font-family: 'Segoe UI', sans-serif;
        color: #ffffff;
    }

    /* Chat container */
    .chat-container {
        max-width: 750px;
        margin: auto;
        padding: 20px 20px 100px 20px; /* bottom padding so input doesn't overlap */
    }

    /* User message bubble */
    .user-msg {
        background-color: #4CAF50;
        color: #ffffff;
        padding: 12px 16px;
        border-radius: 15px 15px 0px 15px;
        margin-bottom: 12px;
        text-align: right;
        margin-left: auto;
        max-width: 70%;
        word-wrap: break-word;
    }

    /* Bot message bubble */
    .bot-msg {
        background-color: #3c3f58;
        color: #ffffff;
        padding: 12px 16px;
        border-radius: 15px 15px 15px 0px;
        margin-bottom: 12px;
        text-align: left;
        margin-right: auto;
        max-width: 70%;
        word-wrap: break-word;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.2);
    }

    /* Input box fixed at bottom */
    .chat-input {
        position: fixed;
        bottom: 15px;
        left: 50%;
        transform: translateX(-50%);
        width: 70%;
        display: flex;
        background: #ffffff;
        border-radius: 30px;
        padding: 8px 15px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.2);
    }

    /* Input field */
    .chat-input input {
        border: none !important;
        flex: 1;
        outline: none !important;
        font-size: 16px;
        padding: 8px;
        color: #000000 !important;
    }

    /* Logo styling */
    .logo {
        text-align: center;
        margin-bottom: 20px;
    }
    .logo img {
        width: 70px;
        border-radius: 50%;
        margin-bottom: 10px;
        box-shadow: 0px 3px 8px rgba(0,0,0,0.3);
    }
    .logo h1 {
        font-weight: 700;
        font-size: 28px;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Logo + Title ---
st.markdown(
    """
    <div class="logo">
        <img src="https://cdn-icons-png.flaticon.com/512/2721/2721261.png" alt="CodeMate Logo">
        <h1>💻 CodeMate</h1>
        <p>Your Friendly Coding Assistant</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize LLM
llm = ChatOpenAI(
    model="llama-3.3-70b-versatile",
    temperature=1,
    openai_api_key="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",
    openai_api_base="https://api.groq.com/openai/v1"
)

# Rules
rules = """
You are a helping assistant for coding. 
Follow these rules strictly:
1. First reply with: "Hey I am your helping assistance".
2. Do not provide full code directly. Only give hints, logic, and step-by-step approach.
3. If the question involves loops, explain how and why loops work in that situation.
4. If the user mentions an error, explain possible reasons for that error and how to fix it.
5. Keep explanations simple and beginner-friendly.
"""

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat display
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{msg["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Input box (Enter to send)
user_input = st.text_input("Type your coding question...", key="chat_input")

if user_input:
    # Add user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Generate bot reply
    prompt = f"{rules}\n\nUser question: {user_input}\n\nYour response:"
    response = llm.predict_messages([HumanMessage(content=prompt)])
    bot_reply = response.content

    # Add bot message
    st.session_state.chat_history.append({"role": "bot", "content": bot_reply})
