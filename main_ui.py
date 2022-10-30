import streamlit as st

from webui.components import create_txt_img_page, create_img_inpaiting_page
from generator.txt_to_img import load_pipeline

if __name__ == '__main__':
    with st.spinner('Loading Model & Components'):
        txt_2_img_pipeline = load_pipeline()

        st.header('Demo for diffusers pipeline')
        st.subheader('By AIS Strategies Sdn Bhd')

        tab1, tab2 = st.tabs(["Text To Image", "Image In Painting"])

        with tab1:
            # Loading widgets
            create_txt_img_page(txt_2_img_pipeline)

        with tab2:
            create_img_inpaiting_page()