# Gerador de Resumos — Documentação Técnica

## Visão Geral

O Gerador de Resumos é um assistente de Inteligência Artificial projetado para facilitar a interpretação de grandes volumes de texto. A aplicação permite ao usuário gerar resumos, extrair palavras-chave e realizar análises personalizadas a partir de textos colados, arquivos PDF ou comandos de voz.

A arquitetura do projeto utiliza um **Agente Local (`ResumoAgent`)**, implementado diretamente com o SDK do Google Gemini. Isso garante maior controle sobre o comportamento do modelo, instruções de sistema mais precisas e uma arquitetura mais leve, sem dependência de frameworks de agentes externos complexos.

---

## Fluxo de Funcionamento

### 1. Entrada de Dados

- **Texto**: O usuário pode colar diretamente o texto na interface.
- **PDF**: O usuário faz upload de um arquivo PDF, que é processado pelo módulo `utils/pdf_handler.py` usando PyPDF para extrair o texto.
- **Voz**: O usuário grava um comando de voz, que é transcrito para texto pelo módulo `utils/audio_handler.py` usando Whisper.

### 2. Comando de Processamento

- O usuário insere um comando (ex: "Resuma este texto em 100 palavras") via texto ou voz.
- O comando é capturado pela interface Streamlit (`app.py`).

### 3. Processamento com Agente Local (`ResumoAgent`)

- O texto extraído e o comando são enviados para o módulo `core.py`.
- A classe `ResumoAgent` recebe a solicitação.
- O agente constrói um prompt estruturado, combinando:
    - **Instruções de Sistema**: Diretrizes de persona, fidelidade e formatação.
    - **Contexto**: O texto fonte fornecido.
    - **Instrução**: O comando específico do usuário.
- O agente envia este prompt otimizado para a API do Google Gemini (modelo `gemini-2.0-flash` ou similar).

### 4. Exibição e Download

- O resultado gerado pelo Gemini é retornado em formato Markdown.
- A interface Streamlit exibe o resultado formatado.
- O usuário pode baixar o resultado em PDF (gerado via WeasyPrint/FPDF) ou como texto simples.

---

## Tecnologias Utilizadas

- **Python 3.12+**
- **Streamlit**: Interface web interativa.
- **Google Generative AI (Gemini)**: Motor de inteligência artificial para análise e geração de texto.
- **OpenAI Whisper**: Transcrição de áudio (Speech-to-Text).
- **PyPDF**: Extração de texto de arquivos PDF.
- **WeasyPrint / FPDF**: Geração de arquivos PDF para download.
- **UV**: Gerenciador de dependências e ambiente virtual.

## Papel das Tecnologias e Integração

- **Streamlit**: Orquestrador da interface e do fluxo de dados. Recebe as entradas do usuário e apresenta as saídas.
- **ResumoAgent (core.py)**: O "cérebro" local da aplicação. É uma abstração que encapsula a comunicação com o Google Gemini, garantindo que todas as requisições sigam um padrão de qualidade e contexto definidos nas instruções do sistema.
- **Google Gemini**: O LLM (Large Language Model) que realiza o processamento cognitivo real do texto.
- **OpenAI Whisper**: Permite a acessibilidade e facilidade de uso através de comandos de voz.
- **PyPDF**: Habilita o processamento de documentos existentes.
- **WeasyPrint**: Converte o resultado (Markdown renderizado como HTML) em um documento PDF profissional para download.

### Integração Detalhada

1. **Usuário** interage com **Streamlit**.
2. **Streamlit** chama `pdf_handler` (se PDF) ou `audio_handler` (se Voz) para preparar os dados brutos.
3. **Streamlit** invoca `generate_response` em `core.py`.
4. `generate_response` delega para a instância global de `ResumoAgent`.
5. **`ResumoAgent`** monta o prompt com suas diretrizes internas e chama `genai.GenerativeModel.generate_content`.
6. **Google Gemini** processa e retorna o texto.
7. **Streamlit** recebe a resposta e usa `pdf_handler` para gerar os arquivos de download.

---

## Estrutura de Classes (Core)

### `ResumoAgent`

Uma classe especializada que mantém a configuração do modelo e as instruções de sistema.

- **`__init__`**: Inicializa o modelo Gemini com `system_instruction` focada em análise de textos, fidelidade e formatação Markdown.
- **`processar(texto_fonte, comando_usuario)`**: Método principal que valida a API Key, constrói o prompt final com separadores claros e executa a chamada à API, tratando erros.

---

## Exemplos de Uso

- "Resuma este artigo em 150 palavras"
- "Extraia as principais palavras-chave"
- "Liste os argumentos centrais do texto"
- "Crie um resumo executivo"
- "Identifique as metodologias mencionadas"

---
