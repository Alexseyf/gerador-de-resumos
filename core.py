import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

class ResumoAgent:
    def __init__(self, model_name='gemini-2.0-flash'):
        self.model_name = model_name
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction="""
Você é um Agente Especialista em Análise e Síntese de Textos.
Sua missão é processar textos fornecidos (artigos, documentos, transcrições) e executar comandos específicos do usuário com alta precisão.

DIRETRIZES DE ATUAÇÃO:
1. **Análise Profunda**: Antes de responder, leia e compreenda todo o contexto do texto fonte.
2. **Fidelidade**: Baseie suas respostas EXCLUSIVAMENTE no texto fornecido. Não invente informações.
3. **Formatação**: Utilize Markdown para estruturar sua resposta. Use títulos, listas (bullets/numéricas), negrito para ênfase e citações quando relevante.
4. **Clareza e Concisão**: Seja direto e objetivo, evitando prolixidade desnecessária, a menos que o usuário peça detalhes.
5. **Adaptabilidade**: Ajuste o tom e o estilo da resposta conforme o comando do usuário (ex: "resumo executivo" vs "explicação para criança").

ESTRUTURA DE RESPOSTA PADRÃO (se não especificado outro formato):
- **Título**: Um título descritivo para a análise.
- **Resumo/Resposta**: O conteúdo principal solicitado.
- **Pontos Chave**: Destaques importantes (se aplicável).
"""
        )

    def processar(self, texto_fonte, comando_usuario):
        if not api_key:
            return "Erro: API Key do Gemini não configurada no arquivo .env"

        prompt = f"""
---
TEXTO FONTE PARA ANÁLISE:
{texto_fonte}
---

COMANDO DO USUÁRIO:
{comando_usuario}

---
Execute o comando acima com base no texto fonte fornecido.
"""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Erro na geração da resposta: {str(e)}"

agent = ResumoAgent()

def generate_response(texto_fonte, comando_usuario):
    if not texto_fonte.strip():
        return "Erro: Nenhum texto foi fornecido para análise."
    if not comando_usuario.strip():
        return "Erro: Nenhum comando foi especificado."
    
    return agent.processar(texto_fonte, comando_usuario)