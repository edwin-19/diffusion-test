from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import time
from fastapi import FastAPI, Request
from webui.html_utils import index_page

from generator.txt_to_img import load_pipeline, generate_img
from api.schema import ImageGenReq, GenResponse

from api.img_utils import image_grid, image_tob64

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:5000",
    "http://localhost:6000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create ai model
txt_to_img_pipeline = load_pipeline()

@app.get('/', response_class=HTMLResponse)
def index():
    return index_page()
    
@app.post('/gen_img', response_model=GenResponse)
async def gen_image(gen_req: ImageGenReq):
    start_time = time.time()
    results = generate_img(
        txt_to_img_pipeline,
        gen_req.prompt, guidance=gen_req.guidance,
        num_inference_steps=gen_req.num_inference_steps,
        seed_val=gen_req.seed_val
    )
    
    # Convert to base 64
    imgs = image_grid(results.images, 1, len(results.images))
    b64_img = image_tob64(imgs)

    end_time = time.time() - start_time
    
    return {
        'img': b64_img,
        'inf_time': end_time
    }