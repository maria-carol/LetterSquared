import streamlit as st

# CABEÇALHO 

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
