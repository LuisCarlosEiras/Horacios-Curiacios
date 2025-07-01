import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(layout="wide")

if "historico" not in st.session_state:
    st.session_state.historico = []

st.markdown("<h1 style='text-align: center;'>⚔️ Os Horácios e os Curiácios ⚔️</h1>", unsafe_allow_html=True)

with open("tabuleiro.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=580, scrolling=False)

col1, col2 = st.columns(2)

with col1:
    if st.button("Zerar histórico do placar"):
        st.session_state.historico.clear()

with col2:
    st.markdown("Resultado das partidas:")
    df = pd.DataFrame(st.session_state.historico, columns=["Resultado"])
    st.dataframe(df, use_container_width=True, hide_index=True)

query_params = st.query_params
if "resultado" in query_params:
    resultado = query_params["resultado"]
    if isinstance(resultado, list):
        resultado = resultado[0]
    if resultado in ["H", "C", "P"]:
        mapa = {"H": "Vitória dos Horácios", "C": "Vitória dos Curiácios", "P": "Paz"}
        st.session_state.historico.append(mapa[resultado])