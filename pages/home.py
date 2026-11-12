import streamlit as st
from pathlib import Path
import base64

def show():
    # 1. Localizar la ruta de assets/home.png desde la raíz del proyecto
    current_dir = Path(__file__).parent.resolve()
    project_root = current_dir.parent
    img_path = project_root / "assets" / "home.png"

    # 2. Cargar y mostrar la imagen centrada antes del texto
    if img_path.exists():
        with open(img_path, "rb") as f:
            encoded_img = base64.b64encode(f.read()).decode("utf-8")
        
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                <img src="data:image/png;base64,{encoded_img}" style="max-width: 100%; width: 350px; border-radius: 12px;">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("No se encontró la imagen en assets/home.png")

    # 3. Mostrar el texto debajo (también centrado si lo deseas)
    st.markdown(
        '<p style="text-align: center; font-size: 1.2rem; color: #111111;">son tuyos. Defiéndelos</p>',
        unsafe_allow_html=True
    )
