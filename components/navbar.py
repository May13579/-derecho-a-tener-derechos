import streamlit as st
from pathlib import Path

def render_navbar():
    # Ruta del logo (ajusta el nombre/archivo según corresponda)
    logo_path = Path("assets/test.jpeg")
    logo_src = logo_path if logo_path.exists() else "https://via.placeholder.com/40"

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
    .top-navbar .logo {{
        height: 44px;
        width: auto;
        border-radius: 8px;
        margin-right: 12px;
    }}

    /* Título junto al logo */
    .top-navbar .brand {{
        color: #ffffff;
        font-size: 1.05rem;
        font-weight: 700;
        margin-right: auto;
        letter-spacing: 0.02em;
    }}

    /* Contenedor de botones */
    .nav-buttons {{
        display: flex;
        gap: 4px;
        align-items: center;
    }}

    /* Botones del navbar */
    .nav-btn {{
        background: transparent !important;
        color: #b0b0b0 !important;
        border: none !important;
        font-size: 0.72rem !important;
        font-weight: 600 !important;
        padding: 6px 10px !important;
        border-radius: 8px !important;
        min-height: auto !important;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        cursor: pointer;
        transition: all 0.2s ease;
    }}
    .nav-btn:hover {{
        background: #2a2a2a !important;
        color: #ffffff !important;
    }}
    .nav-btn.active {{
        background: #1a1a1a !important;
        color: #ffffff !important;
        border: 1px solid #444 !important;
    }}
    </style>

    <div class="top-navbar">
        <img src="{logo_src}" class="logo" alt="Logo" />
        <div class="brand">Derecho a tener derechos</div>
    </div>
    """, unsafe_allow_html=True)

    # Botones de navegación (debajo del HTML del navbar)
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
