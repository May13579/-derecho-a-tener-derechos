import streamlit as st
from pathlib import Path
import base64

def render_navbar():
    # 1. Calcular la ruta absoluta (corregido)
    current_dir = Path(__file__).parent.resolve()
    project_root = current_dir.parent
    logo_path = project_root / "assets" / "test.jpeg"

    logo_src = ""
    
    # 2. Cargar y codificar la imagen en Base64
    if logo_path.exists():
        try:
            with open(logo_path, "rb") as f:
                encoded_logo = base64.b64encode(f.read()).decode("utf-8")
            
            mime_type = "image/jpeg"
            if logo_path.suffix.lower() == ".png":
                mime_type = "image/png"
                
            logo_src = f"data:{mime_type};base64,{encoded_logo}"
        except Exception:
            pass

    # 3. CSS para fijar el navbar negro arriba y estilizar los botones
    st.markdown("""
    <style>
    /* Fijar el bloque de columnas de Streamlit como navbar superior */
    div[data-testid="stHorizontalBlock"] {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        background-color: #000000 !important;
        padding: 8px 16px !important;
        z-index: 9999 !important;
        border-bottom: 1px solid #222;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }

    /* Alinear el contenido de las columnas */
    div[data-testid="stColumn"] {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Empujar el contenido principal hacia abajo para que no lo tape el navbar */
    .block-container {
        padding-top: 75px !important;
    }

    /* Estilo de los botones para que se integren en el fondo negro */
    div[data-testid="stButton"] button {
        background: transparent !important;
        color: #d0d0d0 !important;
        border: 1px solid #333333 !important;
        border-radius: 8px !important;
        font-size: 0.8rem !important;
        font-weight: 600 !important;
        padding: 6px 10px !important;
        transition: all 0.2s ease;
    }
    
    div[data-testid="stButton"] button:hover {
        background: #222222 !important;
        color: #ffffff !important;
        border-color: #555555 !important;
    }

    /* Botón activo (página actual) */
    div[data-testid="stButton"] button[kind="primary"] {
        background: #ffffff !important;
        color: #000000 !important;
        border-color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # 4. Crear las columnas que formarán el navbar
    # La primera columna es para el logo, las demás para los botones
    cols = st.columns([1.2, 1, 1, 1, 1, 1])
    
    with cols[0]:
        if logo_src:
            st.markdown(
                f'<img src="{logo_src}" style="height: 38px; border-radius: 6px; margin-left: 8px;">', 
                unsafe_allow_html=True
            )
        else:
            st.markdown('<div style="font-size: 1.5rem; margin-left: 8px;">⚖️</div>', unsafe_allow_html=True)

    # 5. Botones de navegación
    items = [
        ("Home", "home"),
        ("Derechos", "seleccion"),
        ("Actividad", "actividad"),
        ("CPI", "cpi"),
        ("Config", "configuracion"),
    ]

    for col, (icon, label, page) in zip(cols[1:], items):
        with col:
            is_active = st.session_state.get("current_page") == page
            # Si es la página activa, usamos type="primary" para que el CSS la destaque
            btn_type = "primary" if is_active else "secondary"
            
            if st.button(
                f"{icon} {label}", 
                key=f"nav_{page}", 
                use_container_width=True,
                type=btn_type
            ):
                st.session_state.current_page = page
                st.rerun()
