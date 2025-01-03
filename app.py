import streamlit as st
from lida import Manager, TextGenerationConfig, llm
from dotenv import load_dotenv
import os
from PIL import Image
from io import BytesIO
import base64

# Load environment variables
load_dotenv()

# Initialize the Cohere model
cohere_api_key = os.getenv("COHERE_API_KEY")
if not cohere_api_key:
    st.error("COHERE_API_KEY not found. Please set it in your environment variables.")
    st.stop()

lida = Manager(text_gen=llm("cohere", api_key=cohere_api_key))
textgen_config = TextGenerationConfig(n=1, temperature=0.5, model="command-r-08-2024", use_cache=True)

def base64_to_image(base64_string):
    # Decode the base64 string
    byte_data = base64.b64decode(base64_string)
    # Use BytesIO to convert the byte data to image
    return Image.open(BytesIO(byte_data))

# Streamlit menu
menu = st.sidebar.selectbox("Choose an Option", ["Summarize", "Question based Graph"])

if menu == "Summarize":
    st.subheader("Summarization of your Data")
    file_uploader = st.file_uploader("Upload your CSV", type="csv")
    if file_uploader is not None:
        path_to_save = "filename.csv"
        with open(path_to_save, "wb") as f:
            f.write(file_uploader.getvalue())
        summary = lida.summarize("filename.csv", summary_method="default", textgen_config=textgen_config)
        st.write(summary)
        goals = lida.goals(summary, n=2, textgen_config=textgen_config)
        for goal in goals:
            st.write(goal)
        i = 0
        library = "seaborn"
        textgen_config = TextGenerationConfig(n=1, temperature=0.5, use_cache=True)
        charts = lida.visualize(summary=summary, goal=goals[i], textgen_config=textgen_config, library=library)
        img_base64_string = charts[0].raster
        img = base64_to_image(img_base64_string)
        st.image(img)

elif menu == "Question based Graph":
    st.subheader("Query your Data to Generate Graph")
    file_uploader = st.file_uploader("Upload your CSV", type="csv")
    if file_uploader is not None:
        path_to_save = "filename1.csv"
        with open(path_to_save, "wb") as f:
            f.write(file_uploader.getvalue())
        text_area = st.text_area("Query your Data to Generate Graph", height=200)
        if st.button("Generate Graph"):
            if len(text_area) > 0:
                st.info("Your Query: " + text_area)
                lida = Manager(text_gen=llm("cohere", api_key=cohere_api_key))
                textgen_config = TextGenerationConfig(n=1, temperature=0.5, model="command-r-08-2024", use_cache=True)
                summary = lida.summarize("filename1.csv", summary_method="default", textgen_config=textgen_config)
                user_query = text_area
                charts = lida.visualize(summary=summary, goal=user_query, textgen_config=textgen_config)
                image_base64 = charts[0].raster
                img = base64_to_image(image_base64)
                st.image(img)
