## https://www.youtube.com/watch?v=jGg_1h0qzaM&t=2s


## Setup project
uv init
uv venv --python python3.12
source .venv/Scripts/activate

## importante  Python concepts  - Type Annotations

1. Dictionary
2. typedDict
3. union 
4. optional
5. any
6. lambda function 


# Lang Graaph Element s
 
# 1. state  in langgraph
the state is a dictionary that contains the current state of the application
Analogy : White board


# 2. Nodes in langgraph
 Nodes are the building blocks of a langgraph. They represent a single step in the graph
Nodes are individual functions or operation that perform a specific task
Each node receieves input , porcess it and returns output or an updated state.
Analogy : Assembly line  stations


# 3. Graph in langgraph
 A graph is a collection of nodes that are connected to each other
 The graph is the overall structure of the application.
 Analogy : Road map

# 4. Edges in langgraph
 Edges are the connections between nodes in a graph and define the flow of execution
 Analogy : Train tracks

# 5. Conditional Edges in langgraph
 Conditional edges are used to define the flow of execution based on a condition
 Analogy :Traffic lights

# 6. START node in langgraph
 The START node is the entry point of the graph and is used to define the starting point of the execution
 Analogy : Race Start line

# 7. End node in langgraph
 The End node signifies the conclusion of the workflow in langgraph
 The end node is the final node in the graph and is used to define the end point of the execution
 Analogy : Race Finish line


# 8. Tools in langgraph
 Tools are specialied function or utilities that nodes can utilize to perform specific tasks such as fetch data from an API or perform calculations
 they enchance the functionality of nodes by providing additional capabilities
 Node are part of graph structire and tools are functionalitoies used withing nodes.
  Analogy : Tools in a toolbox : hammer, screwdriver, wrench, etc.


# 9. ToolNode in langgraph
ToolNode is a specialized node that is used to call a tool.
It connects the tool's output back to to the state so other nodes can use the result.
Analogy : Operator using a machine in a factory

# 10. StateGraph in langgraph
A Stategraph is a class in langgraph used to build and compile the graph structure.
It mmanages the nodes, edgesm and overall state , ensuring that the workflow in a unified way and data correctly flow between components.
Analogy : blue print of a building


# 11. Runnable in langgraph
 Runnable in LangGraph is a standardized executable component that performs a specific task with in AI Workflow.
 It serves as a fundamental building block allowing for us creating modular systems.
Analogy  :  lego brick : Just as lego bricks can be snapped to build complex structures, runnables can be combined to create sophisticated AI workflows.


# 12. Message in langgraph
Human Message :  Represents input from a user.
AI Message : Represents output from the AI.
System Message : Represents instructions or context provided to the AI.
Tool Message : Represents the output of a tool used in the workflow.
Function Message : Represents the output of a function used in the workflow.


# Agents
## setup python virtual environment 
py -3.12 --version
py -3.12 -m venv venv
venv\Scripts\activate.bat
python --version

## packages 
pip install langgraph
pip install langchain langchain-community
pip install ollama
pip install -qU langchain-ollama
pip install python-dotenv

pip install pytesseract pdf2image 
pip install setuptools


## Install following ocr 
  
  ### WINSDOWS
https://github.com/UB-Mannheim/tesseract/wiki
tesseract.exe tesseract-ocr-w64-setup-5.5.0.20241111.exe 

### MAC
brew install tesseract
tesseract --version
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract" 



## PaddleOCR
pip install paddleocr
pip install paddlepaddle -f https://www.paddlepaddle.org.cn/whl/simple

## mac : 
pip install paddlepaddle -f https://www.paddlepaddle.org.cn/whl/macos.html


