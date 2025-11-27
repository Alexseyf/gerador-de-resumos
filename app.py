import streamlit as st
import os
from core import generate_response
import utils.pdf_handler as pdf_handler
import utils.audio_handler as audio_handler

st.set_page_config(page_title="Gerador de Resumos", page_icon="📚", layout="wide")

st.title("📚 Gerador de Resumos")
st.markdown("""
Seu assistente de IA para digerir artigos e textos acadêmicos rapidamente.
Cole um texto ou faça upload de um PDF e dê o comando (texto ou voz).
""")

with st.sidebar:
    st.markdown("**Como usar:**")
    st.markdown("1. Cole o texto ou suba um PDF.")
    st.markdown("2. Digite ou fale o comando.")
    st.markdown("3. Clique em Processar Texto.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Entrada")
    input_type = st.radio("Fonte do Texto:", ["Colar Texto", "Upload PDF"])
    
    texto_fonte = ""
    
    if input_type == "Colar Texto":
        texto_fonte = st.text_area("Cole seu texto aqui:", height=300)
    else:
        uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")
        if uploaded_file:
            with st.spinner("Extraindo texto do PDF..."):
                texto_fonte = pdf_handler.extract_text_from_pdf(uploaded_file)
            st.success("PDF carregado com sucesso!")
            with st.expander("Ver texto extraído"):
                st.text(texto_fonte[:500] + "...")

    st.markdown("---")
    st.subheader("🗣️ Comando")
    
    if "comando_texto" not in st.session_state:
        st.session_state.comando_texto = ""

    st.info("💡 **Dica**: Clique no botão, fale e depois clique novamente para parar.")
    audio_value = st.audio_input("Gravar Comando de Voz")
    
    if audio_value is not None:
        try:
            audio_bytes = audio_value.getvalue()
            
            if len(audio_bytes) > 0:
                with st.spinner("🎤 Transcrevendo áudio..."):
                    transcricao = audio_handler.transcribe_audio(audio_bytes)
                    
                    if transcricao and not transcricao.startswith("Erro") and not transcricao.startswith("Whisper"):
                        st.session_state.comando_texto = transcricao
                    else:
                        st.warning(f"⚠️ {transcricao}")
        except Exception as e:
            st.error(f"❌ Erro ao processar áudio: {str(e)}")

    comando_usuario = st.text_input("Digite seu comando:", key="comando_texto", placeholder="Digite aqui sua solicitação ou envie por voz")

with col2:
    st.subheader("📤 Resultado")
    
    if st.button("Processar Texto", type="primary"):
        if not texto_fonte:
            st.warning("Por favor, forneça um texto para processar.")
        elif not comando_usuario:
            st.warning("Por favor, forneça um comando.")
        else:
            with st.spinner("O Agente está processando..."):
                resultado = generate_response(texto_fonte, comando_usuario)
                st.markdown(resultado)

                pdf_bytes = pdf_handler.create_pdf_download(resultado)
                st.download_button("Baixar Resultado (PDF)", data=pdf_bytes, file_name="resumo_agente.pdf", mime="application/pdf")
                st.download_button("Baixar Resultado (Texto)", data=resultado, file_name="resumo_agente.md")

