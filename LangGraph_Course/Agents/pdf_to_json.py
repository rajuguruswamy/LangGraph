import os
from typing import TypedDict, List, Optional, Dict
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage
from langchain_ollama import ChatOllama

import fitz
from PIL import Image
import pytesseract
from paddleocr import PaddleOCR
import numpy as np


# 1. Instantiate llm:
llm = ChatOllama(model="mistral:latest",
                 temperature=0,
                 max_tokens=None,
                 timeout=None,
                 max_retries=2)

# 1. Define the state schema


class TravelDocState(TypedDict):
    file: str
    images: Optional[List[Image.Image]] = None
    text: Optional[str] = None
    structured_data: Optional[str] = None


# 2. Load document (PDF or image)
def load_doc_node(state: TravelDocState) -> TravelDocState:
    """This node load pdf or image and return as image """

    file = state["file"]
    print(f" File name  :  {file}")
    if file.endswith('.pdf'):
        # images = convert_from_path(file)
        doc = fitz.open(file)
        images = [Image.frombytes("RGB", (page.get_pixmap().width, page.get_pixmap(
        ).height), page.get_pixmap().samples) for page in doc]

    else:
        images = [Image.open(file)]

    state["images"] = images
    return state

# 3. Run OCR using pytesseract.


def pytesseract_ocr_node(state: TravelDocState) -> TravelDocState:
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\dilee\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    texts = [pytesseract.image_to_string(img) for img in state["images"]]
    state["text"] = texts
    print(f"state['text']    ============>    {state['text'] } ")
    return state


def PaddleOCR_node(state: TravelDocState) -> TravelDocState:
    # ocr_model = PaddleOCR(use_angle_cls=True, lang='en')
    ocr_model = PaddleOCR(use_textline_orientation=True, lang='en')
    texts = []
    for img in state["images"]:
        print(f"==================> {img}")
        try:
            img_np = np.array(img)
            print(f"==================> {img_np}")
            result = ocr_model.predict(img_np)
            for line in result[0]:
                texts.append(line[1][0])  # Extract the text
        except Exception as e:
            print(f"⚠️ Error processing image with PaddleOCR: {e}")
            texts.append("[ERROR: Unable to OCR this image]")

    state["text"] = texts
    # print(f"state['text'] ============> {state['text']}")
    return state


# 4. Use LLM to extract structured data

def extract_info_node(state: TravelDocState) -> TravelDocState:
    prompt = f"""Extract the following fields from this travel document text:
                - Full Name
                - Passport Number
                - Nationality
                - Date of Birth
                - Expiry Date

                Text:
                {state['text']}

                Return as JSON.
                """
    response = llm.invoke([HumanMessage(content=prompt)])
    state["structured_data"] = response.content
    return state


# 5. Define the graph
builder = StateGraph(TravelDocState)
builder.add_node("load_doc", load_doc_node)
builder.add_node("ocr", pytesseract_ocr_node)
# builder.add_node("ocr", PaddleOCR_node)
builder.add_node("extract_info", extract_info_node)

builder.add_edge(START, "load_doc")
builder.add_edge("load_doc", "ocr")
builder.add_edge("ocr", "extract_info")
builder.add_edge("extract_info", END)

agent = builder.compile()

# 6. Run the pipeline
input_file = "TravelDocument.pdf"  # or .png/.jpg

result = agent.invoke(TravelDocState(file=input_file))
print("📄 Extracted Structured Data:\n")
print(result["structured_data"])
