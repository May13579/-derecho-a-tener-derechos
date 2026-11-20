import streamlit as st
from pathlib import Path

# Diccionario con el color pastel, enlace de video y ruta del PDF de cada derecho
CONTENIDO_DERECHOS = {
    "Derecho a tener derechos": {
        "color": "#B05858",  # Terracota / Rojo apagado
        "video_url": "https://youtube.com",
        "pdf_file": "Derecho.pdf"
    },
    "Derecho a la educación": {
        "color": "#A2D38E",  # Verde pastel
        "video_url": "",
        "pdf_file": "Derecho.pdf"
    },
    "Derecho al acceso a la información": {
        "color": "#FBE987",  # Amarillo pastel
        "video_url": "",
        "pdf_file": "Derecho.pdf"
    },
    "Derecho a la participación política": {
        "color": "#CE6A6B",  # Coral / Salmón
        "video_url": "",
        "pdf_file": "Derecho.pdf"
    },
    "Derecho al acceso a la justicia": {
        "color": "#C7F3EC",  # Menta / Cian claro
        "video_url": "",
        "pdf_file": "Derecho.pdf"
    },
    "Derecho al trabajo": {
        "color": "#82B2BD",  # Azul grisáceo
        "video_url": "",
        "pdf_file": "Derecho.pdf"
    },
    "Derecho a la dignidad": {
        "color": "#EBB5D6",  # Rosa pastel
        "video_url": "",
        "pdf_file": "Derecho.pdf"
    }
}

def show():
    # Recuperar el derecho elegido (por defecto: "Derecho a tener derechos")
    derecho_actual = st.session_state.get("selected_derecho", "Derecho a tener derechos")
    info = CONTENIDO_DERECHOS.get(derecho_actual, CONTENIDO_DERECHOS["Derecho a tener derechos"])
    color_circulo = info["color"]

    # Localizar el archivo PDF en assets/PDF/
    current_dir = Path(__file__).parent.resolve()
    project_root = current_dir.parent
    pdf_path = project_root / "assets" / "PDF" / info["pdf_file"]

    # 1. CSS para replicar el diseño exacto de la imagen (adaptado a stDownloadButton)
    st.html(f"""
    <style>
        @import url('https://googleapis.com');

        /* Contenedor principal centrado */
        .contenedor-pagina-derecho {{
            max-width: 650px;
            margin: 0 auto;
            padding: 0 12px;
        }}

        /* Píldora negra del título con círculo de color a la izquierda */
        .header-pildora-derecho {{
            position: relative;
            background-color: #050505;
            color: #ffffff;
            border-radius: 14px;
            padding: 14px 24px 14px 56px;
            min-height: 54px;
            width: fit-content;
            max-width: 100%;
            display: flex;
            align-items: center;
            margin-left: 12px;
            margin-bottom: 24px;
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.12);
        }}

        .header-pildora-derecho span {{
            font-family: 'Space Mono', 'Courier New', monospace;
            font-size: 1.15rem;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.3;
        }}

        /* Círculo de color con borde negro grueso */
        .header-pildora-derecho::before {{
            content: "";
            position: absolute;
            left: -12px;
            top: 50%;
            transform: translateY(-50%);
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background-color: {color_circulo};
            border: 8px solid #050505;
            box-sizing: content-box;
        }}

        /* Bordes redondeados para el reproductor de video de Streamlit */
        div[data-testid="stVideo"] {{
            max-width: 620px;
            margin: 0 auto 24px auto;
            border-radius: 18px !important;
            overflow: hidden !important;
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.18);
        }}

        /* Centrado del botón rosa "Material Educativo" (stDownloadButton) */
        .st-key-btn_material_edu,
        .st-key-btn_material_edu div[data-testid="stDownloadButton"] {{
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            width: 100% !important;
            margin-top: 8px;
            margin-bottom: 24px;
        }}

        /* Estilo exacto de la píldora rosa "Material Educativo" */
        .st-key-btn_material_edu button {{
            background-color: #EBB5D6 !important;
            color: #050505 !important;
            border: none !important;
            border-radius: 14px !important;
            padding: 12px 28px !important;
            width: auto !important;
            min-width: fit-content !important;
            white-space: nowrap !important;
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease, filter 0.2s ease;
        }}

        .st-key-btn_material_edu button p {{
            font-family: 'Space Mono', 'Courier New', monospace !important;
            font-size: 1.15rem !important;
            font-weight: 700 !important;
            color: #050505 !important;
            margin: 0 !important;
        }}

        .st-key-btn_material_edu button:hover {{
            filter: brightness(0.95);
            transform: translateY(-2px);
        }}

        /* Ajustes responsivos para teléfonos */
        @media (max-width: 768px) {{
            .header-pildora-derecho {{
                padding: 11px 18px 11px 46px;
                min-height: 46px;
                margin-left: 10px;
                margin-bottom: 20px;
            }}
            .header-pildora-derecho span {{
                font-size: 0.95rem;
            }}
            .header-pildora-derecho::before {{
                left: -10px;
                width: 30px;
                height: 30px;
                border-width: 6px;
            }}
            .st-key-btn_material_edu button {{
                padding: 10px 22px !important;
            }}
            .st-key-btn_material_edu button p {{
                font-size: 1rem !important;
            }}
        }}
    </style>
    """)

    # 2. Encabezado en píldora negra con círculo de color
    st.markdown(
        f"""
        <div class="contenedor-pagina-derecho">
            <div class="header-pildora-derecho">
                <span>{derecho_actual}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 3. Video de YouTube (con soporte para marca de tiempo t=22s)
    if info["video_url"]:
        st.video(info["video_url"], start_time=22)
    else:
        st.info("Video educativo próximamente disponible para este derecho.")

    # 4. Botón rosa "Material Educativo" vinculado al archivo PDF
    if pdf_path.exists():
        with open(pdf_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()

        st.download_button(
            label="Material Educativo",
            data=pdf_bytes,
            file_name=info["pdf_file"],
            mime="application/pdf",
            key="btn_material_edu"
        )
    else:
        st.warning(f"No se encontró el archivo en: assets/PDF/{info['pdf_file']}")
