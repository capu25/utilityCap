import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
from pathlib import Path
import base64

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
sample_image = current_dir / ".." / "assets" / "wallaby.png"

st.title("🖌️ BackGround Remover")
st.write("Inserisci la tua immagine e lascia che venga processata!")
st.write("---")

MAX_FILE_SIZE = 5 * 1024 * 1024 #5MB

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format("PNG"))
    byte_im = buf.getvalue()
    return byte_im

def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Modded image :wrench:")
    col2.image(fixed)
    st.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")

col1, col2 = st.columns(2)
my_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    fix_image(sample_image)