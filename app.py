import streamlit as st
import streamlit.components.v1 as components

# Carregar HTML do jogo diretamente no Streamlit
html_code = open("tabuleiro.html", "r", encoding="utf-8").read()

st.set_page_config(page_title="Horácios e Curiácios", layout="centered")

st.markdown("""
## 🎮 Os Horácios e os Curiácios

Este é um protótipo interativo baseado na obra de Brecht, onde você joga com os Horácios (🔵) contra a IA dos Curiácios (🔴).  
Clique nas peças azuis para movê-las e assista à IA reagir automaticamente.

🕹️ Use os botões abaixo do tabuleiro para treinar a IA ou reiniciar a partida.
""")

# Incorporar o HTML com o jogo
components.html(html_code, height=800, scrolling=False)

st.info("Se o tabuleiro não aparecer, clique em 'Reiniciar o jogo'. O resultado final será mostrado abaixo do tabuleiro.")
