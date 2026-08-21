import streamlit as st
from google.cloud import firestore
from menu import render_sidebar_menu

# Chama o menu marcando a opção ativa
render_sidebar_menu(current_page_index=1)

#Conectando a base de dados
dataBase = firestore.Client.from_service_account_json("firebase.json")

st.title("Inserir novo filme na Base de dados")

# --- Formulário de cadastro de filmes
with st.form("formFirebase"):
    titulo = st.text_input("Título:", placeholder="Informe o título...")
    genero = st.text_input("Gênero:", placeholder="Informe o gênero principal...")
    diretor = st.text_input("Diretor:", placeholder="Informe o diretor...")
    rating = st.number_input("Avaliação:", placeholder="Insira a nota média de avaliação...")

    btnSalvarFilme = st.form_submit_button("Salvar", use_container_width=True)

    if btnSalvarFilme:
        if titulo and genero and diretor and rating:
            #Salvar no banco
            novoFilme = dataBase.collection("filmes").document(titulo)
            novoFilme.set(
                {
                    "titulo": titulo,
                    "genero": genero,
                    "diretor": diretor,
                    "rating": rating
                }
            )
            st.success("Filme adicionado!")
        else:
            st.error("Informe título, genero, diretor e avaliação!")