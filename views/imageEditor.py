import streamlit as st
from PIL import Image, ImageEnhance, ImageDraw, ImageOps
import io

st.title("🖼️ Image-Editor")

st.write("Carica un'immagine e trasformala con questo semplice ma efficace editor!")
st.write("---")

uploaded_file = st.file_uploader("Seleziona un'immagine", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption='Immagine caricata', use_column_width=True)

    brightness = st.slider("Modifica la luminosità", 0.1, 3.0, 1.0)

    contrast = st.slider("Modifica il contrasto", 0.1, 3.0, 1.0)

    saturation = st.slider("Modifica la saturazione", 0.1, 3.0, 1.0)

    rotation = st.slider("Ruota l'immagine (gradi)", -180, 180, 0)

    resize_factor = st.slider("Ridimensiona l'immagine (fattore di scala)", 0.1, 2.0, 1.0)

    border_radius = st.slider("Arrotonda i bordi (raggio in pixel)", 0, min(image.size) // 2, 0)

    # --- Applica le modifiche ---
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast)

    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(saturation)

    image = image.rotate(rotation, expand=True)

    width, height = image.size
    image = image.resize((int(width * resize_factor), int(height * resize_factor)))

    if border_radius > 0:
        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle(
            [(0, 0), image.size],
            radius=border_radius,
            fill=255
        )
        image = ImageOps.fit(image, mask.size, centering=(0.5, 0.5))
        image.putalpha(mask)

    st.image(image, caption='Immagine modificata', use_column_width=True)

    buf = io.BytesIO()
    image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Scarica l'immagine modificata",
        data=byte_im,
        file_name="immagine_modificata.png",
        mime="image/png",
    )
