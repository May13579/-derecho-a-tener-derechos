import streamlit as st

def show():
    # CSS para estilizar la lista de botones y adaptarla a teléfonos
    st.html("""
    <style>
        /* Centra el título y subtítulo con buen contraste sobre #D9D9D9 */
        .titulo-seleccion {
            text-align: center;
            color: #111111;
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 5px;
        }
        .subtitulo-seleccion {
            text-align: center;
            color: #333333;
            font-size: 1.1rem;
            margin-bottom: 25px;
        }

        /* Contenedor centrado de la lista */
        .st-key-lista_derechos {
            max-width: 600px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        /* Estilo de cada botón de derecho */
        .st-key-lista_derechos button {
            background-color: #ffffff !important;
            color: #111111 !important;
            border: 1px solid #bbbbbb !important;
            border-radius: 12px !important;
            padding: 14px 20px !important;
            font-size: 1.05rem !important;
            font-weight: 600 !important;
            text-align: left !important;
            justify-content: flex-start !important;
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.08);
            transition: all 0.2s ease;
            width: 100% !important;
        }

        .st-key-lista_derechos button:hover {
            background-color: #FA9ACE !important;
            border-color: #FA9ACE !important;
            transform: translateY(-2px);
            box-shadow: 0 5px 12px rgba(0, 0, 0, 0.15);
        }

        @media (max-width: 768px) {
            .titulo-seleccion {
                font-size: 1.6rem;
            }
            .st-key-lista_derechos button {
                padding: 12px 16px !important;
                font-size: 0.95rem !important;
            }
        }
    </style>
    """)

    # Listado exacto de los 7 derechos
    lista_derechos = [
        "Derecho a tener derechos",
        "Derecho a la educación",
        "Derecho al acceso a la información",
        "Derecho a la participación política",
        "Derecho al acceso a la justicia",
        "Derecho al trabajo",
        "Derecho a la dignidad"
    ]

    # Contenedor aislado para aplicar los estilos solo a esta lista
    with st.container(key="lista_derechos"):
        for idx, derecho in enumerate(lista_derechos):
            if st.button(f"⚖️  {derecho}", key=f"btn_derecho_{idx}", use_container_width=True):
                st.session_state.selected_derecho = derecho
                st.session_state.current_page = "derechos"
                st.rerun()
