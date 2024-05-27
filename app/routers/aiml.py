from fastapi import APIRouter, Request, Response, status, Depends, HTTPException
from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from models import transformers_model_i, salesforse_transformer_model, llama3_model, runwayml_model
import io
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, FileResponse

router = APIRouter()

"""
    A function that handles the POST request to the "/ask/" endpoint.

    Parameters:
        text (str): The text input for the question.
        image (UploadFile): The image file uploaded by the user.

    Returns:
        dict: A dictionary containing the answer to the question.
            The answer is stored under the key "answer".
"""
@router.post("/ask/")
def ask(text:str, image: UploadFile):
    content = image.file.read()
    image = Image.open(io.BytesIO(content))
    
    result = salesforse_transformer_model.predict(text, image)
    json_compatible_item_data = jsonable_encoder({"answer": result})
    return JSONResponse(content=json_compatible_item_data)


@router.post("/generate/image")
def gen_img(text:str):
    # runwayml stable defusion
    # prompt = "a photo of an astronaut riding a horse on mars"

    # image = runwayml_model.generate_diffusion_image(prompt)
    # image.save("output.png")

    # TODO: Add exception handling
    # result = transformers_model_i.predict(text, image)
    # result = salesforse_transformer_model.predict(text, image)
    # genText = llama3_model.generate(text)
    # print(genText)

#     messages = [
#     {"role": "user", "content": "what is the percentage change of the net income from Q4 FY23 to Q4 FY24?"}
# ]

#     document = """NVIDIA (NASDAQ: NVDA) today reported revenue for the fourth quarter ended January 28, 2024, of $22.1 billion, up 22% from the previous quarter and up 265% from a year ago.\nFor the quarter, GAAP earnings per diluted share was $4.93, up 33% from the previous quarter and up 765% from a year ago. Non-GAAP earnings per diluted share was $5.16, up 28% from the previous quarter and up 486% from a year ago.\nQ4 Fiscal 2024 Summary\nGAAP\n| $ in millions, except earnings per share | Q4 FY24 | Q3 FY24 | Q4 FY23 | Q/Q | Y/Y |\n| Revenue | $22,103 | $18,120 | $6,051 | Up 22% | Up 265% |\n| Gross margin | 76.0% | 74.0% | 63.3% | Up 2.0 pts | Up 12.7 pts |\n| Operating expenses | $3,176 | $2,983 | $2,576 | Up 6% | Up 23% |\n| Operating income | $13,615 | $10,417 | $1,257 | Up 31% | Up 983% |\n| Net income | $12,285 | $9,243 | $1,414 | Up 33% | Up 769% |\n| Diluted earnings per share | $4.93 | $3.71 | $0.57 | Up 33% | Up 765% |"""

#     res = llama3_model.get_formatted_response(messages, document)
#     print(res)
    # result = transformers_model_i.predict(text, image)
    return {"message": "Hello World"}
