import typer
from PIL import Image

import requests
import json
import io
import base64

def decode_img(img_b64):
    im_bytes = base64.b64decode(img_b64)
    buf = io.BytesIO(im_bytes)
    img = Image.open(buf)

    return img

def main(
    url:str='http://localhost:8000',
    path:str='/gen_img'
):
    payload = {
        'prompt': ['tokyo tower selfie'] * 2,
        'num_inference_steps': 50,
        'guidance': 7.5,
        'seed_val':  1000
    }

    results = requests.post(
        url + path,
        data=json.dumps(payload) 
    )
    img_b64 = results.json()['img']
    
    # Decode image
    img = decode_img(img_b64)
    img.save('test_output.jpg')

if __name__ == '__main__':
    typer.run(main)