import streamlit as st

def render_navbar():
    st.markdown("""
    <style>
    .navbar {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #ffffff;
        border-top: 1px solid #e0e0e0;
        padding: 8px 0;
        z-index: 999;
        box-shadow: 0 -2px 8px rgba(0,0,0,0.05);
    }
    .nav-item {
        text-align: center;
        padding: 6px 4px;
        cursor: pointer;
        color: #5E6872;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .nav-item .icon { font-size: 1.4rem; display: block; margin-bottom: 2px; }
    .nav-item.active { color: #1B385E; }
    </style>
    """, unsafe_allow_html=True)

    cols = st.columns(6)
    items = [
        ("🏠", "Home", "home"),
        ("📋", "Derechos", "seleccion"),
        ("📖", "Actividad", "actividad"),
        ("📊", "CPI", "cpi"),
        ("⚙️", "Config", "configuracion"),
    ]

    for col, (icon, label, page) in zip(cols, items):
        with col:
            is_active = st.session_state.get("current_page") == page
            if st.button(f"{icon}\n{label}", key=f"nav_{page}", use_container_width=True):
                st.session_state.current_page = page
                st.rerun()