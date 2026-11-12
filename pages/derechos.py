import streamlit as st

# Diccionario con el contenido individual de cada derecho
CONTENIDO_DERECHOS = {
    "Derecho a tener derechos": {
        "descripcion": "Es el principio fundamental que reconoce a toda persona como sujeta de derechos humanos, garantizando su reconocimiento jurídico y dignidad básica en cualquier sociedad.",
        "puntos_clave": [
            "Reconocimiento de la personalidad jurídica.",
            "Base para el ejercicio de todos los demás derechos.",
            "Protección contra la exclusión o invisibilización."
        ]
    },
    "Derecho a la educación": {
        "descripcion": "Garantiza el acceso libre, equitativo y de calidad al aprendizaje y desarrollo integral de las personas en todos los niveles.",
        "puntos_clave": [
            "Acceso gratuito y universal a la educación básica.",
            "Igualdad de oportunidades sin discriminación.",
            "Fomento del pensamiento crítico y desarrollo personal."
        ]
    },
    "Derecho al acceso a la información": {
        "descripcion": "Permite a toda persona buscar, recibir y difundir información pública de manera transparente, oportuna y veraz.",
        "puntos_clave": [
            "Transparencia en la gestión de instituciones públicas.",
            "Acceso a datos sin necesidad de justificar el motivo.",
            "Herramienta clave para la rendición de cuentas."
        ]
    },
    "Derecho a la participación política": {
        "descripcion": "Asegura que la ciudadanía pueda intervenir activamente en los asuntos públicos, elegir representantes y postularse a cargos.",
        "puntos_clave": [
            "Derecho al voto libre, secreto y universal.",
            "Participación en consultas, debates y organizaciones cívicas.",
            "Acceso en condiciones de igualdad a funciones públicas."
        ]
    },
    "Derecho al acceso a la justicia": {
        "descripcion": "Garantiza que toda persona pueda acudir a tribunales independientes e imparciales para defender sus derechos y obtener una resolución justa.",
        "puntos_clave": [
            "Derecho a un debido proceso y defensa legal.",
            "Igualdad ante la ley sin distinciones.",
            "Resolución efectiva y sin dilaciones indebidas."
        ]
    },
    "Derecho al trabajo": {
        "descripcion": "Reconoce la libertad de elegir una ocupación digna, en condiciones seguras, justas y con una remuneración equitativa.",
        "puntos_clave": [
            "Condiciones laborales seguras y saludables.",
            "Salario justo e igualdad de remuneración.",
            "Protección contra el despido injustificado y la explotación."
        ]
    },
    "Derecho a la dignidad": {
        "descripcion": "Es el valor inherente de todo ser humano por el simple hecho de existir, exigiendo respeto, autonomía e integridad física y moral.",
        "puntos_clave": [
            "Trato respetuoso y libre de humillaciones.",
            "Protección de la integridad física, psíquica y moral.",
            "Autonomía para tomar decisiones sobre el propio proyecto de vida."
        ]
    }
}

def show():
    # CSS para la tarjeta de detalle del derecho seleccionado
    st.html("""
    <style>
        .tarjeta-derecho {
            max-width: 750px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 28px;
            border-radius: 16px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            color: #111111;
        }
        .tarjeta-derecho h2 {
            color: #111111;
            margin-top: 0;
            border-bottom: 3px solid #FA9ACE;
            padding-bottom: 10px;
        }
        .tarjeta-derecho p {
            font-size: 1.1rem;
            line-height: 1.6;
            color: #222222;
        }
        .tarjeta-derecho li {
            font-size: 1rem;
            margin-bottom: 8px;
            color: #333333;
        }
        @media (max-width: 768px) {
            .tarjeta-derecho {
                padding: 20px;
            }
            .tarjeta-derecho h2 {
                font-size: 1.4rem;
            }
        }
    </style>
    """)

    # Recuperar el derecho elegido (si entran directo sin elegir, toma el primero por defecto)
    derecho_actual = st.session_state.get("selected_derecho", "Derecho a tener derechos")
    info = CONTENIDO_DERECHOS.get(derecho_actual)

    if info:
        puntos_html = "".join([f"<li>{punto}</li>" for punto in info["puntos_clave"]])
        st.markdown(
            f"""
            <div class="tarjeta-derecho">
                <h2>📖 {derecho_actual}</h2>
                <p>{info["descripcion"]}</p>
                <h4 style="margin-top: 20px; color: #111111;">Aspectos clave:</h4>
                <ul>{puntos_html}</ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("No se encontró información para el derecho seleccionado.")
