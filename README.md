# 📚 Gerador de Resumos

**Atividade - Disciplina de Inteligência Artificial**  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Instituição:** UniSenac

## Sobre o Projeto

O **Gerador de Resumos** é um assistente de IA especializado em auxiliar na interpretação rápida de grandes volumes de texto. O sistema permite processar textos colados diretamente ou extraídos de arquivos PDF, utilizando comandos em texto ou voz para gerar resumos, extrair palavras-chave e realizar outras análises.

O projetoa implementa um **Agente Local (`ResumoAgent`)**, que atua como um especialista dedicado, processando as solicitações com instruções de sistema precisas para garantir fidelidade e qualidade nas respostas, utilizando a API do Google Gemini diretamente.

### Funcionalidades Principais

- ** Processamento de Texto**: Cole texto diretamente ou faça upload de arquivos PDF
- ** Comando por Voz**: Use o Whisper AI para transcrever comandos falados
- ** Agente Especialista**: `ResumoAgent` local powered by Google Gemini para análise contextual
- ** Múltiplos Formatos de Saída**: Resumos, palavras-chave, análises personalizadas
- ** Download de Resultados**: Baixe os resultados em PDF ou texto simples
- ** Interface Web**: Interface amigável construída com Streamlit

##  Tecnologias Utilizadas

- **Python 3.12+**
- **Streamlit** - Interface web interativa
- **Google Generative AI (Gemini)** - Processamento de linguagem natural
- **OpenAI Whisper** - Transcrição de áudio
- **PyPDF** - Extração de texto de PDFs
- **FPDF & WeasyPrint** - Geração de PDFs
- **UV** - Gerenciador de dependências moderno

##  Instalação e Configuração

### Pré-requisitos

1. **Python 3.12 ou superior**
2. **UV (gerenciador de dependências)**

### Instalação do UV

Se você ainda não tem o UV instalado, execute:

```bash
# No Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Ou usando pip
pip install uv
```

### Configuração do Projeto

1. **Clone ou baixe o projeto**
   ```bash
   https://github.com/Alexseyf/gerador-de-resumos.git
   ```

2. **Instale as dependências usando UV**
   ```bash
   uv sync
   ```

3. **Configure a API Key do Google Gemini**  
   Crie o arquivo `.env` na raíz do projeto e adicione sua chave da API do Google Gemini:
   ```
   GEMINI_API_KEY=sua_chave_api_aqui
   ```
   
   > **Como obter a API Key:**
   > 1 - Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
   > 2 - Faça login com sua conta Google
   > 3 - Clique em "Create API Key"
   > 4 - Copie a chave gerada

##  Como Executar

### Usando UV (Recomendado)

```bash
uv run streamlit run app.py
```

### Método Alternativo

```bash
# Ative o ambiente virtual criado pelo UV
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows

# Execute a aplicação
streamlit run app.py
```

A aplicação será aberta automaticamente no navegador em `http://localhost:8501`

##  Como Usar

### 1. **Entrada de Texto**
   - **Colar Texto**: Cole diretamente o texto que deseja processar
   - **Upload PDF**: Faça upload de um arquivo PDF para extração automática do texto

### 2. **Comando**
   - **Texto**: Digite seu comando (ex: "Resuma este texto em 100 palavras")
   - **Voz**: Clique no botão de gravação, fale claramente por 3-5 segundos e pare a gravação

### 3. **Processamento**
   - Clique em "Processar Texto"
   - Aguarde o Agente processar sua solicitação

### 4. **Resultado**
   - Visualize o resultado formatado
   - Baixe em PDF ou texto simples

##  Exemplos de Comandos

- "Resuma este artigo em 150 palavras"
- "Extraia as principais palavras-chave"
- "Liste os argumentos centrais do texto"
- "Crie um resumo executivo"
- "Identifique as metodologias mencionadas"

##  Estrutura do Projeto

```
atividade_final/
├── app.py                # Interface Streamlit principal
├── core.py               # Lógica do Agente Local (ResumoAgent) com Gemini
├── main.py               # Ponto de entrada alternativo
├── pyproject.toml        # Configurações do projeto e dependências
├── uv.lock               # Lock file do UV
├── utils/
│   ├── audio_handler.py  # Processamento de áudio com Whisper
│   └── pdf_handler.py    # Manipulação de PDFs
└── README.md             # Este arquivo
```

##  Dependências Principais

- `streamlit`
- `google-generativeai`
- `openai-whisper`
- `pypdf`
- `fpdf`
- `weasyprint`
- `python-dotenv`

##  Solução de Problemas

### Erro de API Key
```
Erro: API Key do Gemini não configurada
```
**Solução**: Verifique se o arquivo `.env` existe e contém a chave `GEMINI_API_KEY`

### Erro de Dependências
```
ModuleNotFoundError: No module named 'streamlit'
```
**Solução**: Execute `uv sync` para instalar todas as dependências

##  Acadêmicos

Alexandre Seyffert
João Antônio
Miguel Goulart

**Curso**: Análise e Desenvolvimento de Sistemas  
**Instituição**: UniSenac  
**Disciplina**: Inteligência Artificial


Este projeto foi desenvolvido para fins acadêmicos como atividade da disciplina de Inteligência Artificial.


