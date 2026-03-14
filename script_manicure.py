import streamlit as st
import pandas as pd
import logging
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Curso Especialização Manicure", page_icon="💅")

# --- CONFIGURAÇÃO DE LOG ---
def salvar_log_manicure(evento):
    try:
        # Conecta usando a URL da planilha que você enviou
        conn = st.connection("gsheets", type=GSheetsConnection)
        params = st.query_params
        
        # Captura UTMs para o rastreio
        origem = params.get("utm_source", "direto")
        if isinstance(origem, list): origem = origem[0]
        
        cidade = params.get("utm_city", "Indefinida")
        if isinstance(cidade, list): cidade = cidade[0]
        
        novo_log = pd.DataFrame([{
            "Data/Hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "Evento": evento,
            "Origem": origem,
            "Cidade": cidade
        }])
        
        # Lendo e atualizando a "Página1" conforme identificado na sua planilha
        try:
            dados_atuais = conn.read(worksheet="Página1", ttl=0)
            df_final = pd.concat([dados_atuais, novo_log], ignore_index=True)
        except:
            df_final = novo_log
            
        conn.update(worksheet="Página1", data=df_final)
    except Exception as e:
        logging.error(f"Erro no log Manicure: {e}")

# --- INTERFACE DA PRESELL ---
# Substitua pelo seu link real de vendas ou WhatsApp
LINK_VENDAS_MANICURE = "https://seulinkaqui.com" 

st.image("https://images.unsplash.com/photo-1632345031435-8727f6897d53?q=80&w=800")

st.markdown("""
    # ✨ Especialização Avançada: Manicure de Elite
    ### Descubra a técnica que está fazendo manicures faturarem 3x mais com blindagem e esmaltação em gel.
    
    Aperte no botão abaixo para conferir a disponibilidade de vagas e o conteúdo completo do treinamento.
""")

if st.button("✅ QUERO SABER MAIS", use_container_width=True):
    salvar_log_manicure("Clique Saber Mais")
    st.success("Redirecionando para a área de informações...")
    st.markdown(f'<meta http-equiv="refresh" content="1;URL={LINK_VENDAS_MANICURE}">', unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2026 - Suporte ao Profissional de Estética")
