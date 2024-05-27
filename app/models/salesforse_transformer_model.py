from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image


processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def predict(question: str, image: Image):    # prepare inputs
    inputs = processor(image, question, return_tensors="pt")
    out = model.generate(**inputs, max_new_tokens=1000)
    print(processor.decode(out[0], skip_special_tokens=True))
    return processor.decode(out[0], skip_special_tokens=True)