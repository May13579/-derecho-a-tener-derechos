import streamlit as st
from components.navbar import render_navbar
import pages.home as home
import pages.seleccion as seleccion
import pages.derechos as derechos
import pages.actividad as actividad
import pages.cpi as cpi
import pages.configuracion as configuracion

import streamlit as st

st.html("""
<style>
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


#Check

st.set_page_config(
    page_title="Derecho a tener derechos",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Agregar padding inferior para que el navbar no tape contenido
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

# Navbar fijo al final
render_navbar()
