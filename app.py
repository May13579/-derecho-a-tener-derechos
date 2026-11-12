import streamlit as st
from components.navbar import render_navbar
import pages.home as home
import pages.seleccion as seleccion
import pages.derechos as derechos
import pages.actividad as actividad
import pages.cpi as cpi
import pages.configuracion as configuracion

# 1. st.set_page_config siempre debe ir primero
st.set_page_config(
    page_title="Derecho a tener derechos",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. CSS global: fondo #D9D9D9 y ocultamiento de barra superior
st.html("""
<style>
    /* Cambia el color de fondo de toda la pantalla */
    html, body, div[data-testid="stAppViewContainer"], .stApp {
        background-color: #D9D9D9 !important;
    }

    /* Oculta la barra superior (Deploy, menú y línea decorativa) */
    header[data-testid="stHeader"] {
        display: none;
    }

    /* Reduce el espacio en blanco que queda arriba */
    .block-container {
        padding-top: 1rem;
    }
</style>
""")

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Espacio superior para que el navbar fijo no tape el contenido
st.markdown("<div style='height: 110px;'></div>", unsafe_allow_html=True)

# Router
page = st.session_state.current_page
if page == "home":
    home.show()
elif page == "seleccion":
    seleccion.show()
elif page == "derechos":
    derechos.show()
elif page == "actividad":
    actividad.show()
elif page == "cpi":
    cpi.show()
elif page == "configuracion":
    configuracion.show()

# Navbar fijo
render_navbar()
