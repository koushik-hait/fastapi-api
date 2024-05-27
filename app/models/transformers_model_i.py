from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image

# 470MB
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

"""
    Predicts the answer to a given question based on an image.
    Args:
        question (str): The question to be answered.
        image (PIL.Image.Image): The image to be used for prediction.
    Returns:
        str: The predicted answer to the question.
    Raises:
        None
    TODO:
        - Inspect the encoding of the image and question.
        - Test how to get the answer from the model outputs.
"""
def predict(question: str, image: Image):    # prepare inputs
    encoding = processor(image, question, return_tensors="pt")
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    # inspect encoding
    # print("Encoding:", encoding)
    # test how to get the answer
    # print("Model outputs:", outputs)
    # print("Predicted answer:", model.config.id2label[idx])
    return model.config.id2label[idx]
