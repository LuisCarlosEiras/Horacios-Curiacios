import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.set_page_config(page_title="Horácios e Curiácios", layout="centered")

if "historico" not in st.session_state:
    st.session_state.historico = []

# Detectar resultado vindo do HTML
query_resultado = st.query_params.get("resultado", None)
if query_resultado:
    resultado = query_resultado[0]
    if resultado in ["H", "C", "P"]:
        simbolos = {"H": "🏆 Vitória dos Horácios", "C": "🏆 Vitória dos Curiácios", "P": "🤝 Paz"}
        st.session_state.historico.append(simbolos[resultado])
        st.query_params.clear()

# Carregar o tabuleiro
with open("tabuleiro.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=700, scrolling=False)

# Mostrar placar
st.markdown("### Resultado das partidas:")
if st.session_state.historico:
    df = pd.DataFrame(st.session_state.historico, columns=["Resultado"])
    st.dataframe(df, use_container_width=True, hide_index=True)
else:
    st.info("Nenhuma partida foi registrada ainda.")
