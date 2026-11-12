import streamlit as st
from pathlib import Path
import base64

def render_navbar():
    # 1. Calcular la ruta absoluta del logo
    current_dir = Path(__file__).parent.resolve()
    project_root = current_dir.parent
    logo_path = project_root / "assets" / "test.jpeg"

    logo_src = ""
    if logo_path.exists():
        try:
            with open(logo_path, "rb") as f:
                encoded_logo = base64.b64encode(f.read()).decode("utf-8")
            mime_type = "image/png" if logo_path.suffix.lower() == ".png" else "image/jpeg"
            logo_src = f"data:{mime_type};base64,{encoded_logo}"
        except Exception:
            pass

    # 2. CSS aislado usando la clase .st-key-mi_navbar
    st.html("""
    <style>
    /* Oculta la barra superior por defecto */
    header[data-testid="stHeader"] {
        display: none;
    }

    /* Fija el navbar con poco margen lateral (12px) */
    .st-key-mi_navbar {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        width: 100vw !important;
        background-color: #000000 !important;
        padding: 10px 12px !important;
        z-index: 9999 !important;
        border-bottom: 1px solid #222222;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
    }

    /* Asegura que el bloque horizontal use todo el ancho disponible */
    .st-key-mi_navbar div[data-testid="stHorizontalBlock"] {
        width: 100% !important;
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
    }

    /* Columna izquierda (Logo) */
    .st-key-mi_navbar div[data-testid="stColumn"]:first-child {
        display: flex !important;
        justify-content: flex-start !important;
        align-items: center !important;
    }

    /* Columna derecha (Menú): fuerza todos sus hijos internos hacia la derecha */
    .st-key-mi_navbar div[data-testid="stColumn"]:last-child,
    .st-key-mi_navbar div[data-testid="stColumn"]:last-child > div,
    .st-key-mi_navbar div[data-testid="stColumn"]:last-child div[data-testid="stVerticalBlock"],
    .st-key-mi_navbar div[data-testid="stColumn"]:last-child div[data-testid="stElementContainer"] {
        display: flex !important;
        justify-content: flex-end !important;
        align-items: flex-end !important;
        width: auto !important;
        margin-left: auto !important;
        padding-right: 0 !important;
    }

    /* Estilo del botón del menú */
    .st-key-mi_navbar div[data-testid="stPopover"] button {
        background-color: #111111 !important;
        color: #ffffff !important;
        border: 1px solid #333333 !important;
        border-radius: 8px !important;
        padding: 6px 14px !important;
        font-weight: 600 !important;
        margin-right: 0 !important;
    }

    .st-key-mi_navbar div[data-testid="stPopover"] button:hover {
        background-color: #222222 !important;
        border-color: #555555 !important;
    }

    /* Empuja el contenido principal hacia abajo */
    .block-container {
        padding-top: 80px !important;
    }
</style>

    """)

    # 3. Estructura del Navbar: Solo 2 columnas (Izquierda: Logo | Derecha: Menú)
    with st.container(key="mi_navbar"):
        col_logo, col_menu = st.columns([1, 1])

        with col_logo:
            if logo_src:
                st.markdown(
                    f'<img src="{logo_src}" style="height: 38px; border-radius: 6px;">',
                    unsafe_allow_html=True
                )
            else:
                st.markdown('<div style="font-size: 1.5rem; color: white;">⚖️</div>', unsafe_allow_html=True)

        with col_menu:
            # El popover actúa como el menú desplegable en la esquina derecha
            with st.popover("☰ Menú"):
                items = [
                    ("Home", "home"),
                    ("Derechos", "seleccion"),
                    ("Actividad", "actividad"),
                    ("CPI", "cpi"),
                    ("Config", "configuracion"),
                ]

                for label, page in items:
                    is_active = st.session_state.get("current_page") == page
                    btn_type = "primary" if is_active else "secondary"

                    if st.button(
                        label,
                        key=f"nav_{page}",
                        use_container_width=True,
                        type=btn_type
                    ):
                        st.session_state.current_page = page
                        st.rerun()
