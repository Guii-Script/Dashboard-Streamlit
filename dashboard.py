import streamlit as st
import pandas as pd
import plotly.express as px

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Painel de Controle",
    page_icon="🇧🇷",
    layout="wide"
)

# --- CSS CUSTOMIZADO MODERNO ---
st.markdown("""
<style>
    /* Fundo principal com leve gradiente */
    .main {
        background: linear-gradient(135deg, #F5F7FA, #E4EBF5);
        font-family: 'Segoe UI', sans-serif;
    }

    /* Cartões de KPI com efeito glassmorphism */
    .cartao_kpi {
        background: rgba(255, 255, 255, 0.9);
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
        backdrop-filter: blur(8px);
        text-align: left;
        border: 1px solid rgba(255,255,255,0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .cartao_kpi::before {
        content: "";
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(120deg, rgba(255,255,255,0.2), transparent, rgba(255,255,255,0.2));
        transform: rotate(25deg);
        animation: brilho 4s infinite linear;
    }
    @keyframes brilho {
        0% { transform: translateX(-100%) rotate(25deg); }
        100% { transform: translateX(100%) rotate(25deg); }
    }
    .cartao_kpi:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 12px 35px rgba(0,0,0,0.15);
    }
    .cartao_kpi h3 {
        margin: 0;
        color: #5A5A5A;
        font-size: 18px;
        font-weight: 600;
    }
    .cartao_kpi p {
        margin: 8px 0 0 0;
        color: #222;
        font-size: 38px;
        font-weight: bold;
    }
    .cartao_kpi small {
        color: #0B875B;
        font-size: 14px;
        font-weight: 500;
    }

    /* Barras de progresso mais modernas */
    .container_barra_progresso {
        width: 100%;
        background-color: #e6e6e6;
        border-radius: 12px;
        margin: 10px 0;
        overflow: hidden;
    }
    .barra_progresso {
        height: 14px;
        border-radius: 12px;
        text-align: right;
        transition: width 1s ease-in-out;
    }
    .laranja { background: linear-gradient(90deg, #FFB347, #FF7E00); }
    .azul { background: linear-gradient(90deg, #42A5F5, #1565C0); }
    .verde { background: linear-gradient(90deg, #66BB6A, #2E7D32); }

    /* Sidebar mais moderna */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #263238, #1B2428);
        color: white;
    }
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3, 
    section[data-testid="stSidebar"] p {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("📊 PAINEL DE CONTROLE")
    st.markdown("##### 🏠 &nbsp; Início")
    st.markdown("##### 📈 &nbsp; Gráficos")
    st.markdown("##### ⭐ &nbsp; Favoritos")
    st.markdown("##### 💬 &nbsp; Chat")
    st.markdown("##### ⚙️ &nbsp; Configurações")
    st.markdown("##### ❓ &nbsp; Ajuda")
    st.header("Desenvolvimento")
    with st.expander("Seu Menu 01"):
        st.write("Subitem 1.1")
        st.write("Subitem 1.2")
    with st.expander("Seu Menu 02"):
        st.write("Subitem 2.1")

# --- HEADER ---
header_col1, header_col2, header_col3 = st.columns([2, 2, 1])
with header_col1:
    st.markdown("### Painel de Controle > Visão Geral")
with header_col2:
    st.text_input("Search", placeholder="Pesquisar...", label_visibility="collapsed")
with header_col3:
    st.markdown("<div style='text-align: right;'>Olá, João! 👋</div>", unsafe_allow_html=True)

st.divider()

# --- KPIs ---
col1, col2, col3 = st.columns(3, gap="large")
with col1:
    st.markdown("""
    <div class="cartao_kpi">
        <h3>GANHOS (MÊS)</h3>
        <p>R$ 2.723</p>
        <small>+5.2% vs. mês anterior</small>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="cartao_kpi">
        <h3>DOWNLOADS</h3>
        <p>2.142.950</p>
        <small>+12.8% vs. mês anterior</small>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="cartao_kpi">
        <h3>FAVORITOS</h3>
        <p>232.000</p>
        <small>+2.1% vs. mês anterior</small>
    </div>
    """, unsafe_allow_html=True)

# --- GRÁFICO DE LINHA ---
st.subheader("📈 Faturamento Mensal")
dados_linha = pd.DataFrame({
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago'],
    'Valor': [2800, 3500, 3800, 4800, 5800, 5200, 3900, 4500]
})
fig_linha = px.line(dados_linha, x='Mês', y='Valor', markers=True, text='Valor')
fig_linha.update_traces(
    line=dict(color='#42A5F5', width=3),
    marker=dict(color='#42A5F5', size=10),
    texttemplate='%{text:.2s}K', textposition='top center'
)
fig_linha.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor='#E0E0E0'),
    title_x=0.5
)
st.plotly_chart(fig_linha, use_container_width=True)
