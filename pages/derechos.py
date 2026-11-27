import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64
import html

# Diccionario con el color pastel, URL limpia de YouTube y ruta del PDF
CONTENIDO_DERECHOS = {
    "Derecho a tener derechos": {
        "color": "#B05858",  # Terracota / Rojo apagado
        "video_url": "https://www.youtube.com/watch?v=rMizWVmnEZA",
        "pdf_file": "Derecho.pdf",
        "descripcion": [
            'Es la idea de que todas las personas tienen derecho a tener derechos, sin importar su condición política o ideológica.',
            'Con el paso del tiempo, esta noción ha evolucionado hasta convertirse en el reconocimiento de que todas las personas tienen derechos humanos que deben ser reconocidos, garantizados y respetados.',
            'El derecho a tener derechos es el primer derecho, porque permite a todos los individuos, sin excepción, reclamar y exigir que sus derechos sean protegidos.'
        ]
    },
    "Derecho a la educación": {
        "color": "#A2D38E",  # Verde pastel
        "video_url": "https://www.youtube.com/watch?v=fMN7G4piQV0",
        "pdf_file": "Educacion.pdf",
        "descripcion": [
            'La Constitución de Puerto Rico establece que toda persona tiene derecho a una educación que fomente el pleno desarrollo de su personalidad y el fortalecimiento del respeto de los derechos humanos y de las libertades fundamentales.',
            'Requiere, además, que haya un sistema de educación pública que será libre y enteramente no sectario.',
            'La enseñanza será gratuita en la escuela primaria y secundaria y, hasta donde las facilidades del Estado lo permitan, será obligatoria para la escuela primaria.',
            'La Constitución no solo exige que haya acceso a la educación sino que también establece qué tipo de educación se debe recibir: una educación plena.',
            'Es decir, que atienda todos los aspectos de la personalidad humana y que fortalezca el respeto por los derechos humanos.'
        ]
    },
    "Derecho al acceso a la información": {
        "color": "#FBE987",  # Amarillo pastel
        "video_url": "https://www.youtube.com/watch?v=1ZD-S44Y36E",
        "pdf_file": "Informacion.pdf",
        "descripcion": [
            'La información es una herramienta vital para mantener nuestra democracia.',
            'Todas las personas tienen derecho a conocer la información pública que está en manos del Gobierno.',
            'Cuando conocemos la información que afecta nuestras vidas y la de nuestra comunidad, podemos opinar, analizar y participar efectivamente en la toma de decisiones.',
            'Las personas necesitan tener acceso a la información para intercambiar ideas, opinar y tomar decisiones de manera informada y efectiva.',
            'Cuando hablamos de acceso a la información hablamos de que nuestros gobernantes tienen la obligación de administrar el País con transparencia.'
        ]
    },
    "Derecho a la participación política": {
        "color": "#CE6A6B",  # Coral / Salmón
        "video_url": "https://www.youtube.com/watch?v=KL3BpPgW2FY",
        "pdf_file": "Opinion-Politica.pdf",
        "descripcion": [
            'Sin participación política no existe democracia.',
            'En una sociedad democrática, las personas tienen el derecho de participar y decidir sobre las maneras en que se gobierna y administra el País.',
            'El derecho a la participación política debe reconocerse por igual a todas las personas, sin importar su posición social, sexo, raza u otras condiciones.',
            'Cuando hablamos de participación nos referimos a que la toma de decisiones que afectan a las personas y sus comunidades tiene que considerar la experiencia, opinión y voz de los distintos grupos.',
            'No se trata solo de ser escuchados.',
            'Para que la participación política sea verdadera, las propuestas de los distintos grupos deben considerarse y estudiarse con seriedad.'
        ]
    },
    "Derecho al acceso a la justicia": {
        "color": "#C7F3EC",  # Menta / Cian claro
        "video_url": "https://www.youtube.com/watch?v=YurWptHGE5M",
        "pdf_file": "Acceso-Justicia.pdf",
        "descripcion": [
            'El acceso a la justicia es un derecho fundamental que debe garantizarse en una sociedad democrática, participativa e igualitaria.',
            'Es el derecho que tienen todas las personas a utilizar las herramientas y mecanismos legales para que se reconozcan y protejan sus demás derechos.',
            'No existe acceso a la justicia cuando, por motivos económicos, sociales, culturales o políticos, la ley y los sistemas de justicia discriminan contra las personas o grupos.',
            'Sin el acceso a la justicia, otros derechos como el derecho al trabajo, a la educación o al acceso a la información no pueden disfrutarse plenamente ya que, sin esta garantía, las personas no podrían exigir los remedios y protecciones que les corresponden.'
        ]
    },
    "Derecho al trabajo": {
        "color": "#82B2BD",  # Azul grisáceo
        "video_url": "https://www.youtube.com/watch?v=p4gJn6G36VM",
        "pdf_file": "Trabajo.pdf",
        "descripcion": [
            'Todas las personas tienen derecho a seleccionar libremente su trabajo, lo que significa que las condiciones sociales o el género de una persona no deben ser los elementos que definan el empleo que puede desempeñar.',
            'Los patronos, sean empresas privadas o el Gobierno, no pueden discriminar contra una persona que solicita empleo o un trabajador contratado por razón de edad, raza, color, sexo, origen social o nacional, condición social, ideas políticas o religiosas, por ser víctima o ser percibida como víctima de violencia doméstica, agresión sexual o acecho ni por su orientación sexual e identidad de género.',
            'El derecho al trabajo asegura que las personas recibirán una paga digna por su labor.',
            'Además, reconoce el derecho de los trabajadores y trabajadoras a organizarse sindicalmente y a defender sus intereses.',
            'Los patronos deben garantizar que las personas trabajen en ambientes libres de discriminación, seguros y adecuados.'
        ]
    },
    "Derecho a la dignidad": {
        "color": "#EBB5D6",  # Rosa pastel
        "video_url": "https://www.youtube.com/watch?v=yTGCsf9OpmA",
        "pdf_file": "Dignidad.pdf",
        "descripcion": [
            'La dignidad humana es el valor que tienen las personas por el simple hecho de ser personas.',
            'Hay respeto a la dignidad cuando valoramos por igual a las personas, creando las condiciones para que éstas satisfagan sus necesidades básicas y se desarrollen plenamente como seres humanos.',
            'El respeto a la dignidad humana es esencial para la convivencia en una sociedad democrática, participativa e igualitaria, donde los individuos y el Gobierno traten a las personas de manera justa.',
            'La dignidad humana celebra la diversidad.',
            'No hay respeto a la dignidad cuando se discrimina por edad, sexo, raza, condición social, nacionalidad, estado migratorio, orientación sexual, identidad de género, apariencia u otra condición.'
        ]
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

        /* Espacio entre párrafos (una línea en blanco, como en el texto original) */
        .tarjeta-info-derecho .interior p {{
            margin: 0 0 1em 0;
        }}

        .tarjeta-info-derecho .interior p:last-child {{
            margin-bottom: 0;
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
        parrafos_html = "".join(
            f"<p>{html.escape(parrafo)}</p>" for parrafo in info["descripcion"]
        )
        st.html(
            f"""
            <div class="tarjeta-info-derecho">
                <div class="interior">{parrafos_html}</div>
            </div>
            """
        )
