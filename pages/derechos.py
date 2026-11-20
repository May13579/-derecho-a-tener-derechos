import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

# Diccionario con el color pastel, URL limpia de YouTube y ruta del PDF
CONTENIDO_DERECHOS = {
    "Derecho a tener derechos": {
        "color": "#B05858",  # Terracota / Rojo apagado
        "video_url": "https://www.youtube.com/watch?v=rMizWVmnEZA",
        "pdf_file": "Derecho.pdf",
        # TODO: completar el resto del texto (el diseño se corta en "por eso estamos")
        "descripcion": (
            "‘Derechos. Son tuyos. Defiéndelos.’ es una serie de 7 videos y "
            "materiales complementarios que dedicamos a la educación de algunos "
            "derechos humanos universales y derechos constitucionales de Puerto Rico."
            "<br>No se puede defender lo que no se conoce, por eso estamos"
        )
    },
    "Derecho a la educación": {
        "color": "#A2D38E",  # Verde pastel
        "video_url": "https://www.youtube.com/watch?v=fMN7G4piQV0",
        "pdf_file": "Educacion.pdf"
    },
    "Derecho al acceso a la información": {
        "color": "#FBE987",  # Amarillo pastel
        "video_url": "https://www.youtube.com/watch?v=1ZD-S44Y36E",
        "pdf_file": "Informacion.pdf"
    },
    "Derecho a la participación política": {
        "color": "#CE6A6B",  # Coral / Salmón
        "video_url": "https://www.youtube.com/watch?v=KL3BpPgW2FY",
        "pdf_file": "Opinion-Politica.pdf"
    },
    "Derecho al acceso a la justicia": {
        "color": "#C7F3EC",  # Menta / Cian claro
        "video_url": "https://www.youtube.com/watch?v=YurWptHGE5M",
        "pdf_file": "Acceso-Justicia.pdf"
    },
    "Derecho al trabajo": {
        "color": "#82B2BD",  # Azul grisáceo
        "video_url": "https://www.youtube.com/watch?v=p4gJn6G36VM",
        "pdf_file": "Trabajo.pdf"
    },
    "Derecho a la dignidad": {
        "color": "#EBB5D6",  # Rosa pastel
        "video_url": "https://www.youtube.com/watch?v=yTGCsf9OpmA",
        "pdf_file": "Dignidad.pdf"
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

    # 1. CSS para el encabezado, el video nativo st.video y reducir el espacio antes del botón
    st.html(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap');

        /* Espaciador del navbar: en esta página queda en 40px */
        div[data-testid="stMarkdownContainer"] > div[style^="height"]:empty {{
            height: 40px !important;
        }}

        /* Contenedor principal centrado */
        .contenedor-pagina-derecho {{
            max-width: 480px;
            margin: 0 auto;
            padding: 0 0 0 14px; /* Espacio para que el círculo sobresalga, igual que en el menú */
        }}

        /* Píldora negra del título con círculo de color a la izquierda */
        .header-pildora-derecho {{
            position: relative;
            background-color: #050505;
            color: #ffffff;
            border-radius: 14px;
            padding: 14px 22px 14px 56px;
            height: 64px;
            width: 100%;
            box-sizing: border-box;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            text-align: left;
            margin-bottom: 18px;
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.12);
        }}

        .header-pildora-derecho span {{
            font-family: 'Space Mono', 'Courier New', monospace;
            font-size: 1.05rem;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.3;
            text-align: left;
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

        /* Estiliza y redondea el reproductor nativo st.video sin dejar huecos debajo */
        div[data-testid="stVideo"] {{
            max-width: 620px !important;
            margin: 0 auto !important;
            border-radius: 18px !important;
            overflow: hidden !important;
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.18) !important;
        }}

        /* Reduce el margen entre bloques de Streamlit para acercar el botón rosa al video */
        div[data-testid="stElementContainer"]:has(div[data-testid="stVideo"]) {{
            margin-bottom: 8px !important;
        }}

        /* Centra el componente del botón PDF */
        iframe[title="streamlit_components_v1.html_v1"] {{
            display: block !important;
            margin: 0 auto !important;
            max-width: 620px !important;
        }}

        /* Tarjeta de texto: marco negro grueso con interior blanco */
        .tarjeta-info-derecho {{
            max-width: 620px;
            margin: 8px auto 32px auto;
            background-color: #050505;
            border-radius: 22px;
            padding: 10px;
            box-sizing: border-box;
        }}

        .tarjeta-info-derecho .interior {{
            background-color: #ffffff;
            border-radius: 14px;
            padding: 18px 20px;
            font-family: 'Space Mono', 'Courier New', monospace;
            font-size: 1.05rem;
            font-weight: 700;
            line-height: 1.5;
            color: #050505;
        }}

        @media (max-width: 768px) {{
            .header-pildora-derecho {{
                padding: 10px 16px 10px 44px;
                height: 60px;
                margin-bottom: 16px;
            }}
            .header-pildora-derecho span {{
                font-size: 0.9rem;
                line-height: 1.25;
            }}
            .header-pildora-derecho::before {{
                left: -10px;
                width: 30px;
                height: 30px;
                border-width: 6px;
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

    # 3. Video de YouTube con st.video() y URL limpia (altura automática en PC y móvil)
    if info["video_url"]:
        st.video(info["video_url"])
    else:
        st.info("Video educativo próximamente disponible para este derecho.")

    # 4. Botón rosa "Material Educativo" pegado debajo del video
    if pdf_path.exists():
        with open(pdf_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")

        components.html(
            f"""
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap');
                body {{
                    margin: 0;
                    padding: 4px 0 10px 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background: transparent;
                }}
                .btn-pdf {{
                    background-color: #EBB5D6;
                    color: #050505;
                    border: none;
                    border-radius: 14px;
                    padding: 12px 28px;
                    font-family: 'Space Mono', 'Courier New', monospace;
                    font-size: 1.15rem;
                    font-weight: 700;
                    cursor: pointer;
                    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.12);
                    transition: transform 0.2s ease, filter 0.2s ease;
                }}
                .btn-pdf:hover {{
                    filter: brightness(0.95);
                    transform: translateY(-2px);
                }}
            </style>
            <button class="btn-pdf" onclick="abrirPDF()">Material Educativo</button>
            <script>
                function abrirPDF() {{
                    const byteCharacters = atob("{base64_pdf}");
                    const byteNumbers = new Array(byteCharacters.length);
                    for (let i = 0; i < byteCharacters.length; i++) {{
                        byteNumbers[i] = byteCharacters.charCodeAt(i);
                    }}
                    const byteArray = new Uint8Array(byteNumbers);
                    const blob = new Blob([byteArray], {{ type: 'application/pdf' }});
                    const blobUrl = URL.createObjectURL(blob);
                    
                    const nuevaPestana = window.open(blobUrl, '_blank');
                    
                    if (nuevaPestana) {{
                        setTimeout(() => {{
                            try {{
                                nuevaPestana.location.reload();
                            }} catch (e) {{
                                nuevaPestana.location.href = blobUrl;
                            }}
                        }}, 300);
                    }}
                }}
            </script>
            """,
            height=65
        )
    else:
        st.warning(f"No se encontró el archivo en: assets/PDF/{info['pdf_file']}")

    # 5. Tarjeta de descripción (marco negro, interior blanco)
    if info.get("descripcion"):
        st.html(
            f"""
            <div class="tarjeta-info-derecho">
                <div class="interior">{info["descripcion"]}</div>
            </div>
            """
        )
