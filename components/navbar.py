import streamlit as st
from pathlib import Path
import base64

def render_navbar():
    # 1. Calcular la ruta absoluta basada en la ubicación de ESTE archivo
    # Esto evita que falle si ejecutas streamlit desde otra carpeta
    current_dir = Path(__file__).parent.resolve()
    project_root = current_dir.parent
    logo_path = project_root / "assets" / "logo.png"

    logo_html = ""
    
    # 2. Cargar y codificar la imagen
    if logo_path.exists():
        try:
            with open(logo_path, "rb") as f:
                encoded_logo = base64.b64encode(f.read()).decode("utf-8")
            
            # Detectar la extensión para usar el MIME type correcto
            mime_type = "image/png"
            if logo_path.suffix.lower() in [".jpg", ".jpeg"]:
                mime_type = "image/jpeg"
            elif logo_path.suffix.lower() == ".svg":
                mime_type = "image/svg+xml"
                
            logo_html = f'<img src="data:{mime_type};base64,{encoded_logo}" class="logo" alt="Logo" />'
        except Exception as e:
            # Si hay un error al leer, muestra el ícono de respaldo
            logo_html = '<div class="logo-fallback">⚖️</div>'
    else:
        # TEMPORAL: Descomenta la siguiente línea para ver en la app 
        # en qué ruta exacta está buscando el logo.
        # st.warning(f"⚠️ Logo no encontrado en: {logo_path}")
        logo_html = '<div class="logo-fallback">⚖️</div>'

    # 3. Inyectar el HTML y CSS
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
        object-fit: contain;
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

    # 4. Botones de navegación
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
