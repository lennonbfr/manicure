import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------
# CONFIGURAÇÃO
# ---------------------------------------------------

st.set_page_config(
    page_title="Especialização Manicure",
    page_icon="💅",
    layout="centered"
)

LINK_VENDAS_MANICURE = "https://go.hotmart.com/Y104886121U"
PIXEL_ID = "1759073455503460"

# ---------------------------------------------------
# PIXEL META
# ---------------------------------------------------

pixel_code = f"""
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};
if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');

fbq('init', '{PIXEL_ID}');
fbq('track', 'PageView');
</script>

<noscript>
<img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id={PIXEL_ID}&ev=PageView&noscript=1"/>
</noscript>
<!-- End Meta Pixel Code -->
"""
components.html(pixel_code, height=0)

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
# BOTÃO COM EVENTO + REDIRECIONAMENTO
# ---------------------------------------------------

if st.button("👉 VER TREINAMENTO AGORA", use_container_width=True):
    redirect_code = f"""
    <script>
        if (typeof fbq !== 'undefined') {{
            fbq('track', 'ViewContent');
        }}
        window.open('{LINK_VENDAS_MANICURE}', '_self');
    </script>
    """
    components.html(redirect_code, height=0)

# ---------------------------------------------------

st.markdown("---")
st.caption("© 2026 - Suporte ao Profissional de Estética")
