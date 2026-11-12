import streamlit as st

def show():
    # 1. CSS para replicar las píldoras negras con círculo de color a la izquierda
    st.html("""
    <style>
        /* Importa tipografía monoespaciada similar a la imagen */
        @import url('https://googleapis.com');

        /* Contenedor centrado de la lista */
        .st-key-lista_derechos {
            max-width: 480px;
            margin: 10px auto 30px auto;
            display: flex;
            flex-direction: column;
            gap: 22px;
            padding-left: 14px; /* Espacio para que el círculo sobresalga sin cortarse */
        }

        /* Estilo base de cada botón (píldora negra) */
        .st-key-lista_derechos button {
            position: relative !important;
            background-color: #050505 !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 14px !important;
            padding: 14px 22px 14px 56px !important; /* Espacio a la izquierda para el círculo */
            min-height: 54px !important;
            width: fit-content !important;
            max-width: 100% !important;
            text-align: left !important;
            justify-content: flex-start !important;
            align-items: center !important;
            overflow: visible !important; /* Permite que el anillo negro sobresalga */
            box-shadow: 0 3px 6px rgba(0, 0, 0, 0.12);
            transition: transform 0.2s ease, background-color 0.2s ease;
        }

        /* Tipografía monoespaciada blanca dentro del botón */
        .st-key-lista_derechos button p {
            font-family: 'Space Mono', 'Courier New', monospace !important;
            font-size: 1.35rem !important;
            font-weight: 700 !important;
            color: #ffffff !important;
            line-height: 1.3 !important;
            margin: 0 !important;
        }

        .st-key-lista_derechos button:hover {
            transform: translateX(4px);
            background-color: #161616 !important;
        }

        /* Círculo de color con anillo negro que sobresale a la izquierda */
        .st-key-lista_derechos button::before {
            content: "";
            position: absolute;
            left: -12px;
            top: 50%;
            transform: translateY(-50%);
            width: 38px;
            height: 38px;
            border-radius: 50%;
            border: 8px solid #050505; /* Anillo negro grueso */
            box-sizing: content-box;
            z-index: 2;
        }

        /* Colores específicos de cada círculo según la imagen */
        .st-key-btn_derecho_0 button::before { background-color: #B05858; } /* Terracota / Rojo apagado */
        .st-key-btn_derecho_1 button::before { background-color: #A2D38E; } /* Verde pastel */
        .st-key-btn_derecho_2 button::before { background-color: #FBE987; } /* Amarillo pastel */
        .st-key-btn_derecho_3 button::before { background-color: #CE6A6B; } /* Coral / Salmón */
        .st-key-btn_derecho_4 button::before { background-color: #C7F3EC; } /* Menta / Cian claro */
        .st-key-btn_derecho_5 button::before { background-color: #82B2BD; } /* Azul grisáceo */
        .st-key-btn_derecho_6 button::before { background-color: #EBB5D6; } /* Rosa pastel */

        /* Ajustes responsivos para teléfonos */
        /* Ajustes responsivos para teléfonos: bordes negros ajustados al texto */
        @media (max-width: 768px) {
            .st-key-lista_derechos {
                max-width: 100% !important;
                width: 100% !important;
                gap: 16px !important;
                padding-left: 14px !important;
                padding-right: 8px !important;
                align-items: flex-start !important;
            }
        
            /* Evita que las cajas invisibles de Streamlit estiren el botón al 100% */
            .st-key-lista_derechos div[data-testid="stElementContainer"],
            .st-key-lista_derechos div[data-testid="stButton"] {
                width: fit-content !important;
                max-width: 100% !important;
            }
        
            /* Ajusta el borde negro exactamente al tamaño del texto */
            .st-key-lista_derechos button {
                width: fit-content !important;
                max-width: calc(100vw - 44px) !important; /* Evita que se salga de la pantalla */
                min-height: 44px !important;
                height: auto !important;
                padding: 10px 16px 10px 44px !important;
                border-radius: 12px !important;
                display: inline-flex !important;
            }
        
            /* Permite que el texto haga salto de línea limpio sin dejar huecos */
            .st-key-lista_derechos button p {
                font-size: 0.9rem !important;
                line-height: 1.25 !important;
                white-space: normal !important;
                word-break: break-word !important;
            }
        
            /* Proporción del círculo y anillo negro en celular */
            .st-key-lista_derechos button::before {
                left: -10px !important;
                width: 30px !important;
                height: 30px !important;
                border-width: 6px !important;
            }
        }


        
    </style>
    """)

    # 2. Listado exacto de los 7 derechos
    lista_derechos = [
        "Derecho a tener derechos",
        "Derecho a la educación",
        "Derecho al acceso a la información",
        "Derecho a la participación política",
        "Derecho al acceso a la justicia",
        "Derecho al trabajo",
        "Derecho a la dignidad"
    ]

    # 3. Renderizado de cada botón con su key individual
    with st.container(key="lista_derechos"):
        for idx, derecho in enumerate(lista_derechos):
            if st.button(derecho, key=f"btn_derecho_{idx}"):
                st.session_state.selected_derecho = derecho
                st.session_state.current_page = "derechos"
                st.rerun()
