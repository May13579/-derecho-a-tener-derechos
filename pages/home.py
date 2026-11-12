import streamlit as st
from pathlib import Path
import base64

def cargar_imagen_base64(ruta_archivo):
    if ruta_archivo.exists():
        with open(ruta_archivo, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return None

def show():
    # 1. Definir rutas desde la raíz del proyecto
    current_dir = Path(__file__).parent.resolve()
    project_root = current_dir.parent
    assets_dir = project_root / "assets"

    test_img_b64 = cargar_imagen_base64(assets_dir / "test.jpeg")
    home_img_b64 = cargar_imagen_base64(assets_dir / "home.png")

    # 2. CSS para estilizar y centrar el botón rosa (#FA9ACE)
    st.html("""
    <style>
        /* Centra la caja externa y el contenedor interno del botón */
        .st-key-btn_conocelos,
        .st-key-btn_conocelos div[data-testid="stButton"] {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            width: 100% !important;
        }
    
        .st-key-btn_conocelos {
            margin-top: 15px;
        }
    
        /* Estilo del botón rosa #FA9ACE */
        .st-key-btn_conocelos button {
            background-color: #FA9ACE !important;
            color: #111111 !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 10px 28px !important;
            font-size: 1rem !important;
            font-weight: 700 !important;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
            transition: transform 0.2s ease, filter 0.2s ease;
            margin: 0 auto !important;
            width: 20%
        }
    
        .st-key-btn_conocelos button:hover {
            filter: brightness(0.95);
            transform: translateY(-2px);
        }
    </style>

    """)

    # 3. Primera imagen: test.jpeg (centrada)
    if test_img_b64:
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; margin-bottom: 16px;">
                <img src="data:image/jpeg;base64,{test_img_b64}" style="max-width: 100%; width: 300px; border-radius: 12px;">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("No se encontró assets/test.jpeg")

    # 4. Segunda imagen: home.png (centrada)
    if home_img_b64:
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; margin-bottom: 16px;">
                <img src="data:image/png;base64,{home_img_b64}" style="max-width: 100%; width: 350px; border-radius: 12px;">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("No se encontró assets/home.png")

    # 5. Texto centrado
    st.markdown(
        '<p style="text-align: center; font-size: 1.50rem; font-weight: 500; color: #111111; margin-bottom: 10px;">son tuyos. Defiéndelos</p>',
        unsafe_allow_html=True
    )

    # 6. Botón "Conócelos" con color #FA9ACE
    if st.button("Conócelos", key="btn_conocelos"):
        # Acción al hacer clic (por ejemplo, navegar a la página de derechos o selección)
        st.session_state.current_page = "seleccion"
        st.rerun()
