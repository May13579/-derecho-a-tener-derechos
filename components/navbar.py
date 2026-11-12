import streamlit as st
from pathlib import Path
import base64

def render_navbar():
    # 1. Calcular la ruta absoluta
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

    # 3. CSS para navbar con menú hamburguesa
    st.markdown("""
    <style>
    /* Navbar superior fijo */
    .navbar-wrapper {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background-color: #000000;
        z-index: 9999;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }

    .navbar-content {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 12px 20px;
        height: 64px;
    }

    /* Logo */
    .navbar-logo {
        height: 38px;
        border-radius: 6px;
    }

    .logo-fallback {
        font-size: 1.8rem;
    }

    /* Menú desplegable */
    .dropdown-menu {
        position: absolute;
        top: 64px;
        right: 20px;
        background-color: #1a1a1a;
        border-radius: 8px;
        padding: 10px 0;
        min-width: 200px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.4);
        display: none;
    }

    .dropdown-menu.show {
        display: block;
    }

    .menu-item-btn {
        display: block;
        width: 100%;
        padding: 12px 20px;
        background: transparent;
        border: none;
        color: #d0d0d0;
        text-align: left;
        font-size: 0.95rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .menu-item-btn:hover {
        background-color: #2a2a2a;
        color: #ffffff;
    }

    .menu-item-btn.active {
        background-color: #333333;
        color: #ffffff;
        border-left: 3px solid #ffffff;
    }

    /* Empujar el contenido hacia abajo */
    .block-container {
        padding-top: 85px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # 4. Crear el navbar con Streamlit
    col_logo, col_menu = st.columns([3, 1])
    
    with col_logo:
        if logo_src:
            st.markdown(f'<img src="{logo_src}" class="navbar-logo" style="height: 38px; border-radius: 6px;">', unsafe_allow_html=True)
        else:
            st.markdown('<div class="logo-fallback">⚖️</div>', unsafe_allow_html=True)
    
    with col_menu:
        # Botón hamburguesa
        if st.button("☰", key="menu_toggle", help="Menú"):
            st.session_state.show_menu = not st.session_state.get("show_menu", False)
            st.rerun()
        
        # Menú desplegable
        if st.session_state.get("show_menu", False):
            items = [
                ("Home", "home"),
                ("Derechos", "seleccion"),
                ("Actividad", "actividad"),
                ("CPI", "cpi"),
                ("Config", "configuracion"),
            ]
            
            current_page = st.session_state.get("current_page", "home")
            
            for label, page in items:
                is_active = current_page == page
                btn_class = "menu-item-btn active" if is_active else "menu-item-btn"
                
                if st.button(label, key=f"menu_{page}", use_container_width=True):
                    st.session_state.current_page = page
                    st.session_state.show_menu = False
                    st.rerun()
