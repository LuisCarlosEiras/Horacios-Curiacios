import streamlit as st
import streamlit.components.v1 as components

# Carregar HTML do jogo diretamente no Streamlit
html_code = open("tabuleiro.html", "r", encoding="utf-8").read()

st.set_page_config(page_title="Horácios e Curiácios", layout="centered")

st.markdown("""
Este é um protótipo interativo baseado na obra de Brecht, onde você joga com os Horácios (🔵) contra a IA dos Curiácios (🔴).
Clique nas peças azuis para movê-las e assista a IA responder automaticamente.
""")

components.html(html_code, height=800, scrolling=False)

# Exibir resultado final do jogo, se recebido via parâmetro
resultado = st.query_params().get("resultado", [None])[0]
# resultado = st.experimental_get_query_params().get("resultado", [None])[0]
if resultado:
    if resultado == "H":
        st.success("🏆 Vitória dos Horácios!")
    elif resultado == "C":
        st.error("🏆 Vitória dos Curiácios!")
    elif resultado == "P":
        st.warning("🤝 Paz foi alcançada!")

st.info("Recarregue a página para reiniciar o jogo, se necessário.")
