import typer
import torch
from torch import autocast
from matplotlib import pyplot as plt

from diffusers import StableDiffusionPipeline

def main(
    txt_input:str=typer.Option(default=''),
    num_images:int=typer.Option(default=2),
):
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        revision="fp16", 
        torch_dtype=torch.float16,
        use_auth_token=True,
    )
    pipe = pipe.to("cuda")
    pipe.enable_attention_slicing()

    prompt = [txt_input] * num_images
        
    if torch.cuda.is_available():
        with autocast('cuda'):
            torch.cuda.empty_cache() # Ensure app does not explode from memory
            results = pipe(prompt, num_inference_steps=50, height=512, width=512)
    
    plt.figure(figsize=(15, 10))
    for index, image in enumerate(results.images):
        plt.title(txt_input)
        plt.subplot(1, 2, index+1)
        plt.imshow(image)

    plt.savefig('output.jpg')

if __name__ == '__main__':
    typer.run(main)