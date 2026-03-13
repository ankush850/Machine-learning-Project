# Chatbot Using LangChain

**Overview**
- Streamlit chat UI powered by LangChain and OpenAI chat models
- Clean modular architecture under src with configuration and chat service
- Conversation history with system-guided prompt
- Optional terminal CLI for quick interactions

**Architecture**
- Core modules:
  - src/config.py: Loads OPENAI settings from .env
  - src/chat_service.py: ChatOpenAI + prompt + in-memory history
  - app.py: Streamlit chat interface using st.chat_message and st.chat_input
  - cli.py: Simple terminal chat loop
- Defaults:
  - OPENAI_MODEL=gpt-3.5-turbo
  - OPENAI_TEMPERATURE=0.3

**Prerequisites**
- Python 3.10+
- OpenAI API key

**Setup**
- Create and activate venv (recommended)
- Install:
  - pip install -r requirements.txt

**Environment**
- Create .env in project root:
  - OPENAI_API_KEY=your-api-key
  - OPENAI_MODEL=gpt-3.5-turbo
  - OPENAI_TEMPERATURE=0.3
- .env is already ignored via .gitignore

**Run**
- Web UI:
  - streamlit run app.py
- CLI:
  - python cli.py
  - Type /exit to quit

**Features**
- Modern chat models via langchain-openai
- Message memory per session
- Simple, extensible prompt with system role
- Optional Hugging Face Hub dependency for future expansion

**Troubleshooting**

- ModuleNotFoundError for langchain imports:
  - Ensure pip install -r requirements.txt completed successfully
- Authentication error:
  - Verify OPENAI_API_KEY and that your account has access to the specified model
- Streamlit not starting:
  - Check local permissions for the ~/.streamlit directory

**Tech Stack*

- LangChain
- langchain-openai
- Streamlit
- python-dotenv
- huggingface_hub

**Contributing**
- Fork the repo and create a feature branch
- Make changes and open a PR with a clear description

**License**
- This project is licensed under the GNU GPL v3. See LICENSE for details.


