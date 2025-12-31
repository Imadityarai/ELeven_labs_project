# chat_feature.py
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def chat(user_input: str, conversation):
    conversation.append(HumanMessage(content=user_input))
    response = llm.invoke(conversation)
    conversation.append(AIMessage(content=response.content))

    # Summarize if memory grows
    if len(conversation) > 7:
        summary = llm.invoke([
            SystemMessage(content="Summarize briefly"),
            HumanMessage(content="\n".join(m.content for m in conversation))
        ])

        conversation = [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content=f"Conversation summary: {summary.content}")
        ]

    return response, conversation
