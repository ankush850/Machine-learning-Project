import streamlit as st
from src.config import settings
from src.chat_service import ChatService

st.set_page_config(page_title="LangChain ChatBot", page_icon=":earth_americas:", layout="wide")
st.header("LangChain ChatBot")

if "chat_service" not in st.session_state:
    st.session_state["chat_service"] = ChatService(
        api_key=settings.OPENAI_API_KEY,
        model=settings.OPENAI_MODEL,
        temperature=settings.TEMPERATURE,
    )
    st.session_state["messages"] = []

if not settings.OPENAI_API_KEY:
    st.warning("Set OPENAI_API_KEY in .env to use the chatbot")
else:
    for m in st.session_state["messages"]:
        st.chat_message(m["role"]).write(m["content"])

    user_input = st.chat_input("Type a message")
    if user_input:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)
        answer = st.session_state["chat_service"].ask(user_input)
        st.session_state["messages"].append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)
