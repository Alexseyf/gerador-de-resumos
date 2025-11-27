from pypdf import PdfReader
from fpdf import FPDF
import markdown
from weasyprint import HTML
import io

def extract_text_from_pdf(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Erro ao ler PDF: {str(e)}"

def create_pdf_download(markdown_content):
    markdown_content = str(markdown_content)
    try:
        html_content = markdown.markdown(markdown_content, extensions=['extra'])
        full_html = f"""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <title>Resumo Gerado</title>
            <style>
                @page {{
                    size: A4;
                    margin: 2.5cm;
                }}
                
                body {{
                    font-family: 'Arial', sans-serif;
                    line-height: 1.6;
                    color: #333;
                    font-size: 12pt;
                    margin-bottom: 3cm;
                }}
                
                h1 {{
                    color: #2c3e50;
                    font-size: 24pt;
                    margin-bottom: 20px;
                    border-bottom: 2px solid #3498db;
                    padding-bottom: 10px;
                }}
                
                h2 {{
                    color: #34495e;
                    font-size: 18pt;
                    margin-top: 25px;
                    margin-bottom: 15px;
                }}
                
                h3 {{
                    color: #34495e;
                    font-size: 14pt;
                    margin-top: 20px;
                    margin-bottom: 10px;
                }}
                
                p {{
                    text-align: justify;
                    margin-bottom: 12px;
                }}
                
                ul, ol {{
                    margin-left: 20px;
                    margin-bottom: 15px;
                }}
                
                li {{
                    margin-bottom: 5px;
                }}
                
                strong {{
                    color: #2c3e50;
                    font-weight: bold;
                }}
                
                em {{
                    color: #7f8c8d;
                    font-style: italic;
                }}
                
                code {{
                    background-color: #ecf0f1;
                    padding: 2px 4px;
                    border-radius: 3px;
                    font-family: 'Courier New', monospace;
                    font-size: 11pt;
                }}
                
                pre {{
                    background-color: #f8f9fa;
                    border: 1px solid #e9ecef;
                    border-radius: 5px;
                    padding: 15px;
                    overflow-x: auto;
                    font-family: 'Courier New', monospace;
                    font-size: 10pt;
                    line-height: 1.4;
                }}
                
                blockquote {{
                    border-left: 4px solid #3498db;
                    margin-left: 0;
                    padding-left: 20px;
                    color: #555;
                    font-style: italic;
                }}
                
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin: 20px 0;
                }}
                
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }}
                
                th {{
                    background-color: #f2f2f2;
                    font-weight: bold;
                }}
                
                hr {{
                    border: none;
                    border-top: 1px solid #bdc3c7;
                    margin: 25px 0;
                }}
                
                .header {{
                    text-align: center;
                    margin-bottom: 30px;
                    padding-bottom: 20px;
                    border-bottom: 1px solid #ecf0f1;
                }}
                
                .footer {{
                    margin-top: 30px;
                    padding-top: 20px;
                    border-top: 1px solid #ecf0f1;
                    text-align: center;
                    font-size: 10pt;
                    color: #7f8c8d;
                    page-break-inside: avoid;
                }}
            </style>
        </head>
        <body>            
            <div class="content">
                {html_content}
            </div>
            
            <div class="footer">
                Gerado pelo Assistente de IA para Análise de Textos
            </div>
        </body>
        </html>
        """
        html_object = HTML(string=full_html)
        pdf_bytes = html_object.write_pdf()
        
        return pdf_bytes
        
    except Exception as e:
        return create_simple_pdf_fallback(markdown_content, str(e))

def create_simple_pdf_fallback(content, error_msg):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, f"Aviso: Erro na formatacao avancada: {error_msg}", ln=True)
    pdf.cell(0, 10, "Conteudo em formato simples:", ln=True)
    pdf.ln(5)

    simple_text = content.replace('**', '').replace('*', '').replace('#', '').replace('`', '')
    
    try:
        pdf.multi_cell(0, 5, simple_text.encode('latin-1', 'replace').decode('latin-1'))
    except Exception as e:
        pdf.multi_cell(0, 5, f"Erro na codificacao do texto: {str(e)}")
    
    return pdf.output(dest='S').encode('latin-1')
