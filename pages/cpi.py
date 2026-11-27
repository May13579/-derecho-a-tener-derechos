import streamlit as st
from pathlib import Path
import html

IMAGEN = "CPI-square-centered-blackbackground.jpg"

DESCRIPCION = [
    "El Centro de Periodismo Investigativo (CPI) es una entidad sin fines de lucro "
    "creada en 2007 por la periodista Omaya Sosa Pascual, ex presidenta del Overseas "
    "Press Club, y el periodista y abogado Oscar J. Serrano, ex presidente de la "
    "Asociación de Periodistas de Puerto Rico, para fomentar el acceso a la información "
    "del pueblo de Puerto Rico mediante tres vías: el periodismo de investigación, la "
    "litigación y la formación periodística.",

    "El CPI está ubicado en la Escuela de Derecho de la Universidad Interamericana de "
    "Puerto Rico, junto a una clínica legal especializada en derecho a la información. "
    "Por medio de esta, a la vez que se prestan servicios Pro Bono a la comunidad, se "
    "forma a los estudiantes de derecho en este campo en un modelo de aprendizaje "
    "mediante el servicio.",

    "Consciente de la importancia del acceso a la información y de la manera en que ésta "
    "puede ser limitada, el CPI fue creado como instrumento para fomentar y defender este "
    "derecho por dos vías de igual importancia.",
]


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
    </style>
    """)

    # 2. Imagen arriba
    if imagen_path.exists():
        st.image(str(imagen_path))
    else:
        st.warning(f"No se encontró la imagen en: assets/{IMAGEN}")

    # 3. Caja de texto debajo
    parrafos_html = "".join(f"<p>{html.escape(p)}</p>" for p in DESCRIPCION)
    st.html(
        f"""
        <div class="tarjeta-info-derecho">
            <div class="interior">{parrafos_html}</div>
        </div>
        """
    )
