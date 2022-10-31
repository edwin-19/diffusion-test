from typing import List
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

def load_pipeline(
    pipeline_name:str="CompVis/stable-diffusion-v1-4",
    data_type=torch.float16,
    use_auth_token=True, 
    device:str='cuda'
):
    pipe = StableDiffusionPipeline.from_pretrained(
        pipeline_name,
        revision="fp16", 
        torch_dtype=data_type,
        use_auth_token=use_auth_token
    )
    pipe = pipe.to(device)
    pipe.enable_attention_slicing()

    return pipe

def create_latents(pipe, device, seed, height=512, width=512, size:int=1):
    generator = torch.Generator(device=device)
    generator = generator.manual_seed(seed)
    latents = torch.randn(
        (size, pipe.unet.in_channels, height // 8, width // 8),
        generator = generator,
        device = device
    )

    return latents

def generate_img(
    pipeline, prompt:List[str],
    guidance:float, num_inference_steps:int,
    seed_val:int, device:str='cuda'
):
    with autocast(device):
        torch.cuda.empty_cache()

        latents = create_latents(pipeline, device, seed_val, size=len(prompt))
        results = pipeline(
            prompt, num_inference_steps=num_inference_steps, 
            height=512, width=512,
            guidance_scale=guidance,
            latents=latents
        )
        # results = pipeline(
        #     prompt, num_inference_steps=num_inference_steps,
        #     height=512, width=512,
            
        #     # latents = latents,
        # )

    return results