# Chatbot

# Objective :
# 1. Use differnt message types : HumanMessage and AIMessage
# 2. Maintain full conversation history using both message types
# 3. Use Ollama Deepseek model using langchain's ChatOllama
# 4. create shphisticate conversation loop

# Goal : create a form of memory for out Agent
import os
from typing import TypedDict, List, Union
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_ollama import ChatOllama
load_dotenv()

#  create AgentState


class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]


# Instantiate llm:
llm = ChatOllama(model="mistral:latest",
                 temperature=0,
                 max_tokens=None,
                 timeout=None,
                 max_retries=2)


def process(state: AgentState) -> AgentState:
    """This node will solve the request you input"""

    response = llm.invoke(state["messages"])
    state["messages"].append(AIMessage(content=response.content))
    print(f"\nAI: {response.content}")

    return state


# build graph
graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()


# user input
conversation_history = []
user_input = input("Enter: ")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result = agent.invoke({"messages": conversation_history})
    conversation_history = result["messages"]
    user_input = input("Enter: ")


# write conversion history in the file
with open("logging.txt", "w") as file:
    file.write("Your convesational history")

    for message in conversation_history:
        if isinstance(message, HumanMessage):
            file.write(f"You : {message.content}\n")
        elif isinstance(message, AIMessage):
            file.write(f"AI: {message.content}\n\n")
    file.write("End of conversation")

print("Conversation saved to logging.txt")
