# Simple BOT

# Objective :

# 1. Defibe State Structure with list of HumanMessage Object
# 2. Initilaize Ollama Deepseek model using langchain's ChatOllama
# 3. sending and handling differetnt type of  messages
# 4. Building and compiling the graph of the Agent

# Main Goal  : How to integrate LLMS in our graph

from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

load_dotenv()


class AgentState(TypedDict):
    messages: List[HumanMessage]


# Instantiate llm:
llm = ChatOllama(model="deepseek-r1:1.5b",
                 temperature=0,
                 max_tokens=None,
                 timeout=None,
                 max_retries=2)


def process(state: AgentState) -> AgentState:
    # invoke llm
    response = llm.invoke(state["messages"])
    print(f"\n AI: {response.content}")
    return state


# build graph
graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END,)
agent = graph.compile()


# user input
user_input = input("Enter: ")
while user_input != "exit":
    agent.invoke({"messages": [HumanMessage(content=user_input)]})
    user_input = input("Enter: ")
