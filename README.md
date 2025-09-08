## CodeMate – Your Friendly Coding Assistant

CodeMate is an interactive coding assistant built using Streamlit and LangChain.
It provides beginner-friendly guidance, step-by-step problem-solving approaches, and error explanations in a clean, chatbot-style interface.

🚀 Features

🤖 AI-Powered Help – Uses LLaMA-based models for coding assistance.

📝 Step-by-Step Explanations – Offers logic, hints, and approaches (not direct solutions).

🔁 Loop Explanations – Special focus on explaining loops and their usage.

🐞 Error Fixing Guidance – Identifies possible causes of coding errors and suggests fixes.

🎨 Custom Chat UI – Modern, styled chat bubbles for user & bot messages.

💾 Persistent Chat History – Keeps conversation context within the session.

🛠️ Tech Stack

Python

Streamlit – Frontend & UI

LangChain – LLM integration

Groq API – LLaMA-3.3 model backend

📦 Installation

Create a virtual environment:

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

⚙️ Configuration

In app.py, update your Groq API key:

openai_api_key = "your_groq_api_key"


If you don’t have a key, create one at Groq Cloud
.

📂 Project Structure
.
├── app.py             # Main Streamlit app
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

📖 Usage

Start the app with streamlit run app.py.

Type your coding-related question in the input box.

Get beginner-friendly explanations, hints, and debugging help.

💡 Note: CodeMate will never provide direct full solutions—it focuses on teaching how and why.

🔮 Future Improvements

✅ Add support for multiple programming languages

✅ Export chat history

✅ Dark/Light theme toggle

✅ Voice-based interaction
