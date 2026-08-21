import streamlit as st
from menu import render_sidebar_menu

# Chama o menu marcando a opção ativa
render_sidebar_menu(current_page_index=0)

# CABEÇALHO HOME

#Criando colunas para img + título
col_logo, col_titulo = st.columns([1, 5], vertical_alignment="center")

#Logotipo
with col_logo:
    st.image("img/logotipo.png", width=120)

#Título e subtítulo
with col_titulo:
    st.title("LetterSquared")

st.subheader(
    "Sua plataforma preferida para filmes, reviews e informações que são 'Absolute CINEMA'!", 
    divider=True
)
