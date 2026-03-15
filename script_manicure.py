import streamlit as st

# ---------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# ---------------------------------------------------

st.set_page_config(
    page_title="Especialização Manicure",
    page_icon="💅",
    layout="centered"
)

# ---------------------------------------------------
# LINK DE VENDA
# ---------------------------------------------------

LINK_VENDAS_MANICURE = "https://go.hotmart.com/Y104886121U"

# ---------------------------------------------------
# CSS
# ---------------------------------------------------

st.markdown("""
<style>
.stApp {
    background-color: #fffafc;
}

.block-container {
    max-width: 760px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

.headline {
    font-size: 2rem;
    font-weight: 700;
    line-height: 1.25;
    color: #111827;
    margin-top: 1rem;
    margin-bottom: 0.7rem;
}

.subheadline {
    font-size: 1.1rem;
    color: #374151;
    margin-bottom: 1.2rem;
}

.benefit-box {
    background: #ffffff;
    border: 1px solid #f3d6e3;
    border-radius: 16px;
    padding: 18px;
    margin: 18px 0;
    box-shadow: 0 4px 18px rgba(0,0,0,0.04);
}

.cta-note {
    background: #fff1f7;
    border: 1px solid #f9c5dc;
    border-radius: 14px;
    padding: 16px;
    color: #7a284b;
    margin: 18px 0;
    font-size: 0.98rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# INTERFACE
# ---------------------------------------------------

st.image(
    "https://images.unsplash.com/photo-1632345031435-8727f6897d53?q=80&w=1200",
    use_container_width=True
)

st.markdown(
    '<div class="headline">A técnica que está ajudando manicures a cobrar mais por atendimento</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subheadline">Descubra como a blindagem e a esmaltação em gel podem valorizar seu serviço, aumentar a percepção de qualidade e ajudar você a sair do básico.</div>',
    unsafe_allow_html=True
)

st.markdown("""
### Esse treinamento foi pensado para manicures que querem:

- **aumentar o valor do atendimento**
- **oferecer um serviço mais valorizado**
- **aprender blindagem e esmaltação em gel**
- **se diferenciar das profissionais que fazem o básico**
- **ter mais segurança na hora de cobrar**
""")

st.markdown(
    """
    <div class="benefit-box">
        <strong>Por que isso importa?</strong><br><br>
        Muitas manicures continuam cobrando barato não porque trabalham mal,
        mas porque ainda não dominam técnicas que deixam o serviço mais valorizado
        aos olhos da cliente.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="cta-note">
        Clique no botão abaixo para ver como funciona o treinamento completo.
    </div>
    """,
    unsafe_allow_html=True
)

st.link_button(
    "💅 VER TREINAMENTO AGORA",
    LINK_VENDAS_MANICURE,
    use_container_width=True
)

st.markdown("---")
st.caption("© 2026 - Suporte ao Profissional de Estética")
