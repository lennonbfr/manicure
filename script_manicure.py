import streamlit as st
import pandas as pd
import logging
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Curso Especialização Manicure", page_icon="💅")

# --- FUNÇÃO DE LOG ---
def salvar_log_manicure(evento):

    try:
        conn = st.connection("gsheets", type=GSheetsConnection)

        params = st.query_params

        origem = params.get("utm_source", "direto")
        if isinstance(origem, list):
            origem = origem[0]

        cidade = params.get("utm_city", "Indefinida")
        if isinstance(cidade, list):
            cidade = cidade[0]

        novo_log = pd.DataFrame([{
            "Data/Hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "Evento": evento,
            "Origem": origem,
            "Cidade": cidade
        }])

      def salvar_log_manicure(evento):

    try:
        conn = st.connection("gsheets", type=GSheetsConnection)

        params = st.query_params

        origem = params.get("utm_source", "direto")
        if isinstance(origem, list):
            origem = origem[0]

        cidade = params.get("utm_city", "Indefinida")
        if isinstance(cidade, list):
            cidade = cidade[0]

        novo_log = pd.DataFrame([{
            "Data/Hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "Evento": evento,
            "Origem": origem,
            "Cidade": cidade
        }])

        conn.append(worksheet="Página1", data=novo_log)

    except Exception as e:
        st.error(e)
    except Exception as e:
        logging.error(f"Erro no log Manicure: {e}")


# --- REGISTRO AUTOMÁTICO DE VISITA ---
if "visit_logged" not in st.session_state:
    salvar_log_manicure("Visualizou Página")
    st.session_state.visit_logged = True


# --- INTERFACE DA PRESELL ---

LINK_VENDAS_MANICURE = "https://go.hotmart.com/Y104886121U"

st.image("https://images.unsplash.com/photo-1632345031435-8727f6897d53?q=80&w=800")

st.markdown("""
# ✨ Especialização Avançada: Manicure de Elite

### Descubra a técnica que está fazendo manicures faturarem 3x mais com blindagem e esmaltação em gel.

Aperte no botão abaixo para conferir a disponibilidade de vagas e o conteúdo completo do treinamento.
""")


# --- BOTÃO PRINCIPAL ---
if st.button("✅ QUERO SABER MAIS", use_container_width=True):

    salvar_log_manicure("Clique Saber Mais")

    st.success("Perfeito! Clique no link abaixo para abrir a página oficial:")

    st.markdown(f"""
    <a href="{LINK_VENDAS_MANICURE}" target="_blank" style="text-decoration: none;">
        <div style="
            background-color:#25d366;
            color:white;
            padding:15px;
            text-align:center;
            border-radius:10px;
            font-weight:bold;
            font-size:20px;
        ">
        👉 CLIQUE AQUI PARA VER AS VAGAS 👈
        </div>
    </a>
    """, unsafe_allow_html=True)


st.markdown("---")
st.caption("© 2026 - Suporte ao Profissional de Estética")
