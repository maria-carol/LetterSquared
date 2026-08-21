import streamlit as st
from streamlit_option_menu import option_menu

def render_sidebar_menu(current_page_index=0):
    #Oculta o menu nativo
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                display: none !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.sidebar:
        selected = option_menu(
            menu_title="LetterSquared",
            options=["Início", "Cadastrar", "Acervo", "Sobre"],
            icons=["house", "plus-circle", "film", "info-circle"],
            menu_icon="camera-reels",
            default_index=current_page_index,
        )

    #Redireciona se o usuário clicar em uma página diferente da atual
    rotas = {
        "Início": (0, "streamlit_app.py"),
        "Catálogo": (1, "pages/01_Cadastrar.py"),
        "Cadastrar": (2, "pages/02_Acervo.py"),
        "Reviews": (3, "pages/03_Sobre.py"),
    }

    indice_escolhido, caminho_arquivo = rotas[selected]

    # Evita que a página recarregue a si mesma infinitamente
    if indice_escolhido != current_page_index:
        st.switch_page(caminho_arquivo)