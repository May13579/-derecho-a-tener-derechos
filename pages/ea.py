import streamlit as st
from pathlib import Path
import html
import re

IMAGEN = "Derechos.png"

# Los enlaces se escriben con la sintaxis [texto](url) y se convierten en <a> al mostrarlos
DESCRIPCION = [
    "Espacios Abiertos es una organización sin fines de lucro, independiente y no "
    "partidista que busca crear y fortalecer mecanismos de participación cívica para "
    "que las personas en Puerto Rico puedan incidir directa y efectivamente en los "
    "procesos sociales, políticos y económicos del país. Aspiramos a una sociedad "
    "abierta, transparente y participativa que sea más justa y equitativa para todas "
    "y todos en Puerto Rico.",

    "EA se creó en febrero de 2014, luego de un año de trabajo resultado de una "
    "invitación de [Open Society Foundations](https://www.opensocietyfoundations.org/) "
    "en 2013 para Puerto Rico participar de una propuesta competitiva (Open Places "
    "Initiative) entre 16 jurisdicciones de EEUU. En la creación de EA, junto al "
    "[Centro para una Nueva Economía](http://grupocne.org/), participaron "
    "[ACLU Puerto Rico](http://aclu-pr.org/), el "
    "[Centro de Periodismo Investigativo](http://periodismoinvestigativo.com/) y la "
    "[Clínica de Asistencia Legal de la Escuela de Derecho de la UPR]"
    "(http://derecho.uprrp.edu/clinica/). Desde 2019 Espacios Abiertos Puerto Rico es "
    "una organización completamente independiente, reconocida como organización exenta "
    "bajo la sección 501(c)(3) del Código de Rentas Internas Federal, así como exenta a "
    "nivel local bajo el Código de Rentas Internas de Puerto Rico.",
]


def a_html(texto):
    """Escapa el texto y convierte [texto](url) en enlaces que abren en pestaña nueva."""
    seguro = html.escape(texto)
    return re.sub(
        r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        seguro,
    )


def show():
    # Localizar la imagen en assets/
    current_dir = Path(__file__).parent.resolve()
    project_root = current_dir.parent
    imagen_path = project_root / "assets" / IMAGEN

    # 1. CSS: imagen centrada y tarjeta de texto (mismo estilo que la página de cada derecho)
    st.html("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap');

        /* Espaciador del navbar: misma altura que en la página de cada derecho */
        div[data-testid="stMarkdownContainer"] > div[style^="height"]:empty {
            height: 40px !important;
        }

        /* Imagen del CPI centrada con esquinas redondeadas */
        div[data-testid="stImage"] {
            max-width: 480px !important;
            margin: 0 auto !important;
            border-radius: 18px !important;
            overflow: hidden !important;
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.18) !important;
        }

        div[data-testid="stImage"] img {
            width: 100% !important;
            height: auto !important;
            display: block;
        }

        /* Tarjeta de texto: marco negro grueso con interior blanco */
        .tarjeta-info-derecho {
            max-width: 620px;
            margin: 24px auto 32px auto;
            background-color: #050505;
            border-radius: 22px;
            padding: 10px;
            box-sizing: border-box;
        }

        .tarjeta-info-derecho .interior {
            background-color: #ffffff;
            border-radius: 14px;
            padding: 18px 20px;
            font-family: 'Space Mono', 'Courier New', monospace;
            font-size: 1.05rem;
            font-weight: 700;
            line-height: 1.5;
            color: #050505;
        }

        /* Espacio entre párrafos */
        .tarjeta-info-derecho .interior p {
            margin: 0 0 1em 0;
        }

        .tarjeta-info-derecho .interior p:last-child {
            margin-bottom: 0;
        }

        .tarjeta-info-derecho .interior a {
            color: #050505;
            text-decoration: underline;
            text-underline-offset: 3px;
        }

        .tarjeta-info-derecho .interior a:hover {
            opacity: 0.7;
        }
    </style>
    """)

    # 2. Imagen arriba
    if imagen_path.exists():
        st.image(str(imagen_path))
    else:
        st.warning(f"No se encontró la imagen en: assets/{IMAGEN}")

    # 3. Caja de texto debajo
    parrafos_html = "".join(f"<p>{a_html(p)}</p>" for p in DESCRIPCION)
    st.html(
        f"""
        <div class="tarjeta-info-derecho">
            <div class="interior">{parrafos_html}</div>
        </div>
        """
    )
