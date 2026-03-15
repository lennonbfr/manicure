import streamlit as st

# ---------------------------------------------------
# CONFIGURAÇÃO
# ---------------------------------------------------

st.set_page_config(
    page_title="Especialização Manicure",
    page_icon="💅",
    layout="centered"
)

LINK_VENDAS_MANICURE = "https://go.hotmart.com/Y104886121U"

# ---------------------------------------------------
# CSS
# ---------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #0b1220;
}

.block-container {
    max-width: 760px;
}

.headline {
    font-size: 2.1rem;
    font-weight: 700;
    color: white;
    margin-top: 20px;
}

.subheadline {
    font-size: 1.2rem;
    color: #d1d5db;
    margin-top: 10px;
}

.benefits {
    margin-top: 18px;
    color: #e5e7eb;
    font-size: 1rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# IMAGEM
# ---------------------------------------------------

st.image(
    "https://images.unsplash.com/photo-1632345031435-8727f6897d53?q=80&w=1200",
    use_container_width=True
)

# ---------------------------------------------------
# HEADLINE
# ---------------------------------------------------

st.markdown(
    '<div class="headline">💅 A técnica que está ajudando manicures a cobrar mais por atendimento</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# SUBTEXTO
# ---------------------------------------------------

st.markdown(
    '<div class="subheadline">Descubra como a blindagem e a esmaltação em gel podem valorizar seu serviço e aumentar o valor do atendimento.</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# BENEFÍCIOS
# ---------------------------------------------------

st.markdown("""
<div class="benefits">

Esse treinamento foi pensado para manicures que querem:

✔ aumentar o valor do atendimento  
✔ aprender blindagem e esmaltação em gel  
✔ oferecer um serviço mais valorizado  
✔ se diferenciar de manicures que fazem apenas o básico  
✔ ter mais segurança na hora de cobrar  

</div>
""", unsafe_allow_html=True)

st.write("")

st.write("Clique abaixo para ver como funciona o treinamento completo.")

# ---------------------------------------------------
# BOTÃO DIRETO PARA OFERTA
# ---------------------------------------------------

st.link_button(
    "👉 VER TREINAMENTO AGORA",
    LINK_VENDAS_MANICURE,
    use_container_width=True
)

# ---------------------------------------------------

st.markdown("---")
st.caption("© 2026 - Suporte ao Profissional de Estética")
