from click import prompt
import streamlit as st
import requests
import json

from webui.web_utils import decode_b64

def create_txt_img_page():
    st.header("Text To Image")

    options = st.selectbox(
        'Example prompts',
        ('Beach house with cartoon vibes', 'Tokyo tower of pikachu eating')
    )

    text_prompt = st.text_area(
        label='Input Prompt for Image Generation',
        value=options
    )
    button_clicked = st.button('Generate')

    with st.expander("Advance Options"):
        # Input for advance options
        col1, col2, col3 = st.columns(3)
        
        with col1:
            image_num = st.slider('Number of images', 1, 2, 1)

        with col2:
            inf_steps = st.slider('Infernce Steps', 1, 100, 50)

        with col3:
            guidance_scale = st.slider('Guidance Scale', 0.0, 30.0, 7.5)

        seed_val = st.slider('Seed', 0, 100000, 2000)
    
    if button_clicked:
        with st.spinner('Generating Image'):
            payload = {
                'prompt': [text_prompt] * image_num,
                'num_inference_steps': inf_steps,
                'guidance': guidance_scale,
                'seed_val':  seed_val
            }
            url = 'http://localhost:8000/gen_img'
            results = requests.post(
                url, data=json.dumps(payload) 
            )
            img_b64 = results.json()['img']
            img = decode_b64(img_b64)

            st.image(img, caption=text_prompt)
    
def create_img_inpaiting_page():
    st.header('Image Inpainting')