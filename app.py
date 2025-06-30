import streamlit as st
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="Horácios e Curiácios", layout="centered")
st.title("Jogo: Os Horácios e os Curiácios")

defaults = {
    'pecas': {},
    'donos': {},
    'turno': 'H',
    'vitorias_h': 0,
    'vitorias_c': 0,
    'empates': 0,
    'historico_curiacio': [],
    'selecionado': None
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
linhas = list(range(8, 0, -1))

# Estado inicial
def estado_inicial():
    pecas = {
        'C8': '🏹', 'D8': '🏹', 'E8': '🏹',
        'C7': '🗡️', 'D7': '🗡️', 'E7': '🗡️',
        'C6': '⚔️', 'D6': '⚔️', 'E6': '⚔️',
        'C1': '🏹', 'D1': '🏹', 'E1': '🏹',
        'C2': '🗡️', 'D2': '🗡️', 'E2': '🗡️',
        'C3': '⚔️', 'D3': '⚔️', 'E3': '⚔️'
    }
    donos = {pos: ('C' if int(pos[1]) >= 6 else 'H') for pos in pecas}
    st.session_state.pecas = pecas
    st.session_state.donos = donos
    st.session_state.turno = 'H'
    st.session_state.selecionado = None

# Movimentos válidos
def gerar_movimentos_validos(origem):
    pecas = st.session_state.pecas
    donos = st.session_state.donos
    tipo = pecas[origem]
    movimentos = []
    col0 = ord(origem[0])
    row0 = int(origem[1])
    alcance = 3 if tipo == '🏹' else 2 if tipo == '🗡️' else 1
    for dx in range(-alcance, alcance + 1):
        for dy in range(-alcance, alcance + 1):
            if dx == 0 and dy == 0:
                continue
            col = chr(col0 + dx)
            row = row0 + dy
            destino = col + str(row)
            if 'A' <= col <= 'G' and 1 <= row <= 8:
                if destino not in pecas or donos.get(destino) != donos[origem]:
                    movimentos.append(destino)
    return movimentos

# Jogada IA
def jogada_ia():
    pecas = st.session_state.pecas
    donos = st.session_state.donos
    melhor, peso = None, -1
    for origem in list(pecas):
        if donos[origem] != 'C':
            continue
        for destino in gerar_movimentos_validos(origem):
            p = random.random() + (1 if destino in pecas else 0)
            if p > peso:
                melhor = (origem, destino)
                peso = p
    if melhor:
        origem, destino = melhor
        pecas[destino] = pecas[origem]
        donos[destino] = 'C'
        del pecas[origem]
        del donos[origem]
    st.session_state.turno = 'H'

# Verifica fim
def verificar_fim():
    donos = st.session_state.donos
    vivos_h = sum(1 for d in donos.values() if d == 'H')
    vivos_c = sum(1 for d in donos.values() if d == 'C')
    if vivos_h == 0:
        st.session_state.vitorias_c += 1
        st.session_state.historico_curiacio.append(st.session_state.vitorias_c)
        return 'C'
    elif vivos_c == 0:
        st.session_state.vitorias_h += 1
        return 'H'
    elif vivos_h == 1 and vivos_c == 1:
        st.session_state.empates += 1
        return 'E'
    return None

# Reiniciar
if st.button("🔄 Reiniciar Jogo"):
    estado_inicial()

# Tabuleiro com botões e estilo
st.markdown("<style>div[data-testid='column'] > div {text-align: center}</style>", unsafe_allow_html=True)
for row in linhas:
    cols = st.columns(len(letras))
    for i, col in enumerate(cols):
        coord = letras[i] + str(row)
        peca = st.session_state.pecas.get(coord, '')
        dono = st.session_state.donos.get(coord, '')
        cor_fundo = '#f0d9b5' if (row + i) % 2 == 0 else '#b58863'
        selecionado = st.session_state.get("selecionado")
        estilo = f"background-color:{cor_fundo}; font-size:28px; height:48px; border:none; width:100%"
        if coord == selecionado:
            estilo += "; border: 3px solid red"

        with col:
            if st.button(peca if peca else " ", key=coord):
                if selecionado:
                    if coord in gerar_movimentos_validos(selecionado):
                        st.session_state.pecas[coord] = st.session_state.pecas[selecionado]
                        st.session_state.donos[coord] = 'H'
                        del st.session_state.pecas[selecionado]
                        del st.session_state.donos[selecionado]
                        st.session_state.selecionado = None
                        st.session_state.turno = 'C'
                        resultado = verificar_fim()
                        if resultado is None:
                            jogada_ia()
                            verificar_fim()
                    else:
                        st.session_state.selecionado = None
                elif peca and dono == 'H':
                    st.session_state.selecionado = coord
            st.markdown(f"<div style='{estilo}'>{peca if peca else '&nbsp;'}</div>", unsafe_allow_html=True)

# Placar
st.markdown(f"""
### Placar:
- 🔵 Horácios: {st.session_state.vitorias_h}
- 🔴 Curiácios: {st.session_state.vitorias_c}
- 🤝 Empates: {st.session_state.empates}
""")

# Gráfico
def plotar_grafico():
    fig, ax = plt.subplots()
    ax.plot(range(1, len(st.session_state.historico_curiacio)+1),
            st.session_state.historico_curiacio, marker='o', color='red')
    ax.set_title("Vitórias dos Curiácios")
    ax.set_xlabel("Treinamentos")
    ax.set_ylabel("Vitórias acumuladas")
    st.pyplot(fig)

plotar_grafico()
 
