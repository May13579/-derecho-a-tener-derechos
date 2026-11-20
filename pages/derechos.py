import streamlit as st
from pathlib import Path
import base64

# Diccionario con el color pastel, ID del video de YouTube y ruta del PDF
CONTENIDO_DERECHOS = {
    "Derecho a tener derechos": {
        "color": "#B05858",  # Terracota / Rojo apagado
        "youtube_id": "rMizWVmnEZA",
        "start_time": 22,
        "pdf_file": "Derecho.pdf"
    },
    "Derecho a la educación": {
        "color": "#A2D38E",  # Verde pastel
        "youtube_id": "",
        "start_time": 0,
        "pdf_file": "Derecho.pdf"
    },
    "Derecho al acceso a la información": {
        "color": "#FBE987",  # Amarillo pastel
        "youtube_id": "",
        "start_time": 0,
        "pdf_file": "Derecho.pdf"
    },
    "Derecho a la participación política": {
        "color": "#CE6A6B",  # Coral / Salmón
        "youtube_id": "",
        "start_time": 0,
        "pdf_file": "Derecho.pdf"
    },
    "Derecho al acceso a la justicia": {
        "color": "#C7F3EC",  # Menta / Cian claro
        "youtube_id": "",
        "start_time": 0,
        "pdf_file": "Derecho.pdf"
    },
    "Derecho al trabajo": {
        "color": "#82B2BD",  # Azul grisáceo
        "youtube_id": "",
        "start_time": 0,
        "pdf_file": "Derecho.pdf"
    },
    "Derecho a la dignidad": {
        "color": "#EBB5D6",  # Rosa pastel
        "youtube_id": "",
        "start_time": 0,
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

    # 1. CSS para el encabezado, el reproductor de YouTube y la píldora rosa
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

        /* Contenedor responsivo 16:9 para que el video de YouTube siempre cargue */
        .video-wrapper {{
            position: relative;
            width: 100%;
            max-width: 620px;
            margin: 0 auto 28px auto;
            aspect-ratio: 16 / 9;
            border-radius: 18px;
            overflow: hidden;
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.18);
            background-color: #000000;
        }}

        .video-wrapper iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }}

        /* Contenedor centrado de la píldora rosa */
        .contenedor-boton-pdf {{
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            margin-top: 8px;
            margin-bottom: 30px;
        }}

        /* Enlace estilizado como píldora rosa "Material Educativo" */
        a.pildora-material-edu {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            background-color: #EBB5D6 !important;
            color: #050505 !important;
            text-decoration: none !important;
            border-radius: 14px;
            padding: 12px 28px;
            font-family: 'Space Mono', 'Courier New', monospace;
            font-size: 1.15rem;
            font-weight: 700;
            white-space: nowrap;
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.12);
            transition: transform 0.2s ease, filter 0.2s ease;
        }}

        a.pildora-material-edu:hover {{
            filter: brightness(0.95);
            transform: translateY(-2px);
            color: #050505 !important;
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
            a.pildora-material-edu {{
                padding: 10px 22px;
                font-size: 1rem;
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

    # 3. Reproductor de YouTube incrustado directamente (100% confiable en móvil y PC)
    if info["youtube_id"]:
        yt_id = info["youtube_id"]
        start = info["start_time"]
        st.markdown(
            f"""
            <div class="video-wrapper">
                <iframe 
                    src="https://youtube.com{yt_id}?start={start}&rel=0" 
                    title="{derecho_actual}"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen>
                </iframe>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.info("Video educativo próximamente disponible para este derecho.")

    # 4. Píldora rosa "Material Educativo" que abre el PDF en una pestaña nueva
    if pdf_path.exists():
        with open(pdf_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")

        st.markdown(
            f"""
            <div class="contenedor-boton-pdf">
                <a href="data:application/pdf;base64,{base64_pdf}" target="_blank" rel="noopener noreferrer" class="pildora-material-edu">
                    Material Educativo
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning(f"No se encontró el archivo en: assets/PDF/{info['pdf_file']}")
