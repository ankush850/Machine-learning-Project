from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

class ChatService:
    def __init__(self, api_key: str, model: str, temperature: float = 0.3):
        self.llm = ChatOpenAI(api_key=api_key, model=model, temperature=temperature)
        self.history = []
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a helpful assistant"),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{input}"),
            ]
        )

    def ask(self, text: str) -> str:
        messages = self.prompt.format_messages(history=self.history, input=text)
        ai = self.llm.invoke(messages)
        self.history.append(HumanMessage(content=text))
        self.history.append(ai)
        return ai.content
