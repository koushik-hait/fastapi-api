from diffusers import StableDiffusionPipeline
import torch

model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")

def generate_diffusion_image(prompt):
    # prompt = "a photo of an astronaut riding a horse on mars"
    image = pipe(prompt).images[0]  
        
    image.save("generated_output.png")
    return image