import streamlit as st
import streamlit.components.v1 as components
import os

# Ajuste 1: Configuração da página para layout centralizado (padrão)
st.set_page_config(page_title="Horácios e Curiácios")

# Ajuste 1: Centralização do título usando HTML no markdown
st.markdown("<h1 style='text-align: center;'>Os Horácios e os Curiácios</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Você 🔵 X IA 🔴</h3>", unsafe_allow_html=True)

# Resultado da partida
resultado = st.query_params.get("resultado", [None])[0]

if resultado:
    st.success(f"Resultado da última partida: {'Vitória dos Horácios' if resultado=='H' else 'Vitória dos Curiácios' if resultado=='C' else 'Paz'}")

# Caminho para o HTML do tabuleiro
html_path = os.path.join(os.path.dirname(__file__), "tabuleiro.html")

# Renderiza o HTML
with open(html_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

components.html(html_content, height=800, scrolling=True)
