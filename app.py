import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Horácios e Curiácios", layout="centered")
# st.title("Jogo: Os Horácios e os Curiácios")

with open("tabuleiro.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=1000, scrolling=False)
