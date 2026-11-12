import streamlit as st
from pathlib import Path
import base64

def render_navbar():
    # 1. Calcular la ruta absoluta del logo
    current_dir = Path(__file__).parent.resolve()
    project_root = current_dir.parent
    logo_path = project_root / "assets" / "Derechos.png"

    logo_src = ""
    if logo_path.exists():
        try:
            with open(logo_path, "rb") as f:
                encoded_logo = base64.b64encode(f.read()).decode("utf-8")
            mime_type = "image/png" if logo_path.suffix.lower() == ".png" else "image/jpeg"
            logo_src = f"data:{mime_type};base64,{encoded_logo}"
        except Exception:
            pass

    # 2. CSS completo y ordenado
    st.html("""
    <style>
        /* Oculta la barra superior por defecto */
        header[data-testid="stHeader"] {
            display: none;
        }

        /* Fija el navbar arriba */
        .st-key-mi_navbar {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            width: 100vw !important;
            background-color: #000000 !important;
            padding: 10px 16px !important;
            z-index: 9999 !important;
            border-bottom: 1px solid #222222;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
        }

        /* Evita que las columnas se apilen en teléfonos */
        .st-key-mi_navbar div[data-testid="stHorizontalBlock"] {
            width: 100% !important;
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important;
            justify-content: space-between !important;
            align-items: center !important;
            gap: 8px !important;
        }

        /* Centra verticalmente todos los contenedores internos de ambas columnas */
        .st-key-mi_navbar div[data-testid="stColumn"] > div,
        .st-key-mi_navbar div[data-testid="stVerticalBlock"],
        .st-key-mi_navbar div[data-testid="stElementContainer"],
        .st-key-mi_navbar div[data-testid="stMarkdownContainer"] {
            display: flex !important;
            align-items: center !important;
            margin-bottom: 0 !important;
            padding-bottom: 0 !important;
            min-height: 0 !important;
        }

        /* Columna izquierda (Logo) */
        .st-key-mi_navbar div[data-testid="stColumn"]:first-child {
            width: auto !important;
            min-width: fit-content !important;
            flex: 0 1 auto !important;
            display: flex !important;
            justify-content: flex-start !important;
            align-items: center !important;
        }

        /* Elimina el espacio fantasma debajo de la imagen y fija su altura */
        .st-key-mi_navbar img {
            display: block !important;
            height: 38px !important;
            width: auto !important;
            margin: 0 !important;
            object-fit: contain;
        }

        /* Columna derecha (Menú): empuja el botón al extremo derecho */
        .st-key-mi_navbar div[data-testid="stColumn"]:last-child,
        .st-key-mi_navbar div[data-testid="stColumn"]:last-child > div,
        .st-key-mi_navbar div[data-testid="stColumn"]:last-child div[data-testid="stVerticalBlock"],
        .st-key-mi_navbar div[data-testid="stColumn"]:last-child div[data-testid="stElementContainer"] {
            width: auto !important;
            min-width: fit-content !important;
            flex: 0 1 auto !important;
            display: flex !important;
            justify-content: flex-end !important;
            align-items: center !important;
            margin-left: auto !important;
            padding-right: 0 !important;
        }

        /* Estilo del botón del menú con la misma altura que el logo (38px) */
        .st-key-mi_navbar div[data-testid="stPopover"] button {
            height: 38px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            background-color: #111111 !important;
            color: #ffffff !important;
            border: 1px solid #333333 !important;
            border-radius: 8px !important;
            padding: 0 14px !important;
            margin: 0 !important;
            font-weight: 600 !important;
            white-space: nowrap !important;
        }

        .st-key-mi_navbar div[data-testid="stPopover"] button:hover {
            background-color: #222222 !important;
            border-color: #555555 !important;
        }

        /* Empuja el contenido principal hacia abajo */
        .block-container {
            padding-top: 80px !important;
        }

        /* Ajustes específicos para pantallas de teléfono (siempre al final) */
        @media (max-width: 768px) {
            .st-key-mi_navbar {
                padding: 8px 12px !important;
            }
            
            /* Iguala altura del logo y el botón a 32px en móvil */
            .st-key-mi_navbar img {
                height: 32px !important;
            }

            .st-key-mi_navbar div[data-testid="stPopover"] button {
                height: 32px !important;
                padding: 0 10px !important;
                font-size: 0.85rem !important;
            }

            .block-container {
                padding-top: 68px !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }
        }
    </style>
    """)

    # 3. Estructura del Navbar
    with st.container(key="mi_navbar"):
        col_logo, col_menu = st.columns([1, 1])

        with col_logo:
            if logo_src:
                st.markdown(
                    f'<img src="{logo_src}" style="border-radius: 6px;">',
                    unsafe_allow_html=True
                )
            else:
                st.markdown('<div style="font-size: 1.5rem; color: white; line-height: 1;">⚖️</div>', unsafe_allow_html=True)

        with col_menu:
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
