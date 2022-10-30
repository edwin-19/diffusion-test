import streamlit as st
from generator.txt_to_img import generate_img

def create_txt_img_page(pipeline):
    st.header("Text To Image")

    st.write('Examples')
    options = st.selectbox(
        'Choose an option to as a prompt',
        ('Beach house with cartoon vibes', 'Tokyo tower of pikachu eating')
    )

    text_prompt = st.text_area(
        label='Input Prompt for Image Generation',
        value='Tokyo Tower Selfie'
    )
    option = st.button('Generate')

    with st.expander("Advance Options"):
        # Input for advance options
        col1, col2, col3 = st.columns(3)
        
        with col1:
            image_num = st.slider('Number of images', 1, 10, 1)

        with col2:
            inf_steps = st.slider('Infernce Steps', 1, 50, 1)

        with col3:
            guidance_scale = st.slider('Guidance Scale', 0.0, 30.0, 7.5)

        seed_val = st.slider('Seed', 0, 100000, 2000)
    
    # prompt = [text_prompt] * image_num
    prompt = ['justin bieber playing cards', 'selena gomez jumping']
    print('Generating image')
    results = generate_img(
        pipeline, prompt, guidance_scale,
        inf_steps, seed_val
    )
    image = results.images[0]
    st.image(image, caption=text_prompt)
    
def create_img_inpaiting_page():
    st.header('Image Inpainting')