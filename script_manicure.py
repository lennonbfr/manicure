import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# ---------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ---------------------------------------------------

st.set_page_config(
    page_title="Especialização Manicure",
    page_icon="💅",
    layout="centered"
)

# ---------------------------------------------------
# FUNÇÃO DE LOG
# ---------------------------------------------------

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

        try:
            dados_atuais = conn.read(worksheet="Página1", ttl=0)
            df_final = pd.concat([dados_atuais, novo_log], ignore_index=True)
        except:
            df_final = novo_log

        conn.update(worksheet="Página1", data=df_final)

    except Exception as e:
        st.error(f"Erro ao salvar log: {e}")


# ---------------------------------------------------
# REGISTRA VISUALIZAÇÃO DA PÁGINA
# ---------------------------------------------------

if "log_visualizacao" not in st.session_state:
    salvar_log_manicure("Visualizou Página")
    st.session_state.log_visualizacao = True


# ---------------------------------------------------
# LINK DE VENDA
# ---------------------------------------------------

LINK_VENDAS_MANICURE = "https://go.hotmart.com/Y104886121U"


# ---------------------------------------------------
# INTERFACE
# ---------------------------------------------------

st.image(
    "https://images.unsplash.com/photo-1632345031435-8727f6897d53?q=80&w=1200"
)

st.markdown("""
# ✨ Especialização Avançada para Manicures

### Descubra a técnica que está fazendo manicures faturarem **até 3x mais** com blindagem e esmaltação em gel.

Esse treinamento foi criado para manicures que querem:

✔ Atrair clientes premium  
✔ Cobrar mais pelos serviços  
✔ Dominar técnicas modernas de blindagem e gel  

Clique no botão abaixo para ver **como funciona o treinamento completo**.
""")


# ---------------------------------------------------
# BOTÃO PRINCIPAL
# ---------------------------------------------------

if st.button("💅 QUERO SABER MAIS", use_container_width=True):

    salvar_log_manicure("Clique Saber Mais")

    st.success("Perfeito! Clique no botão abaixo para acessar a página oficial do treinamento.")

    st.markdown(f"""
    <a href="{LINK_VENDAS_MANICURE}" target="_blank" style="text-decoration:none;">
        <div style="
            background-color:#e91e63;
            color:white;
            padding:16px;
            text-align:center;
            border-radius:10px;
            font-size:20px;
            font-weight:bold;
        ">
        👉 VER TREINAMENTO AGORA
        </div>
    </a>
    """, unsafe_allow_html=True)


st.markdown("---")
st.caption("© 2026 - Suporte ao Profissional de Estética")
