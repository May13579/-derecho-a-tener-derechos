import streamlit as st
from pathlib import Path
import base64

def render_navbar():
    # 1. Cargar y codificar la imagen
    logo_path = Path("assets/test.jpeg")  # 👈 Asegúrate que tu imagen esté aquí
    logo_html = ""
    
    if logo_path.exists():
        with open(logo_path, "rb") as f:
            encoded_logo = base64.b64encode(f.read()).decode("utf-8")
        # Creamos la etiqueta img con la imagen incrustada
        logo_html = f'<img src="data:image/png;base64,{encoded_logo}" class="logo" alt="Logo" />'
    else:
        # Si no encuentra la imagen, muestra un texto o ícono por defecto
        logo_html = '<div class="logo-fallback">⚖️</div>'

    # 2. Inyectar el HTML y CSS
    st.markdown(f"""
    <style>
    /* Navbar superior fijo */
    .top-navbar {{
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 64px;
        background: #000000;
        display: flex;
        align-items: center;
        padding: 0 16px;
        z-index: 9999;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }}

    /* Logo esquina superior izquierda */
    .logo {{
        height: 44px;
        width: auto;
        border-radius: 8px;
        margin-right: 12px;
    }}
    
    /* Fallback si no hay imagen */
    .logo-fallback {{
        font-size: 1.8rem;
        margin-right: 12px;
    }}

    /* Título junto al logo */
    .brand {{
        color: #ffffff;
        font-size: 1.05rem;
        font-weight: 700;
        margin-right: auto;
        letter-spacing: 0.02em;
    }}
    </style>

    <div class="top-navbar">
        {logo_html}
        <div class="brand">Derecho a tener derechos</div>
    </div>
    """, unsafe_allow_html=True)

    # 3. Botones de navegación
    cols = st.columns(5)
    items = [
        ("🏠", "Home", "home"),
        ("📋", "Derechos", "seleccion"),
        ("🎯", "Actividad", "actividad"),
        ("📊", "CPI", "cpi"),
        ("⚙️", "Config", "configuracion"),
    ]

    for col, (icon, label, page) in zip(cols, items):
        with col:
            is_active = st.session_state.get("current_page") == page
            if st.button(
                f"{icon} {label}",
                key=f"nav_{page}",
                use_container_width=True,
            ):
                st.session_state.current_page = page
                st.rerun()
