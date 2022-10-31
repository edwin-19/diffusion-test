from PIL import Image
from io import BytesIO
import base64

def decode_b64(img_b64) -> Image.Image:
    im_bytes = base64.b64decode(img_b64)
    buf = BytesIO(im_bytes)
    img = Image.open(buf)

    return img