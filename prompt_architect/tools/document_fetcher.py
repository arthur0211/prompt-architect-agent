import os
from pathlib import Path

def fetch_document_content(file_path: str):
    """
    Lê o conteúdo de documentos locais de texto.
    
    Args:
        file_path: Caminho para o arquivo
        
    Returns:
        dict: Resultado com status e conteúdo do arquivo
    """
    try:
        file_path = Path(file_path)
        
        if not file_path.exists():
            return {
                "status": "error",
                "file_path": str(file_path),
                "error": "Arquivo não encontrado"
            }
            
        if not file_path.is_file():
            return {
                "status": "error",
                "file_path": str(file_path),
                "error": "Caminho não é um arquivo"
            }
            
        # Verificar se é um tipo de arquivo suportado
        supported_extensions = {'.txt', '.md', '.py', '.js', '.json', '.xml', '.html', '.css', '.yaml', '.yml'}
        if file_path.suffix.lower() not in supported_extensions:
            return {
                "status": "error",
                "file_path": str(file_path),
                "error": f"Tipo de arquivo não suportado: {file_path.suffix}"
            }
            
        # Ler o conteúdo
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        return {
            "status": "success",
            "file_path": str(file_path),
            "content": content
        }
        
    except Exception as e:
        return {
            "status": "error",
            "file_path": str(file_path),
            "error": str(e)
        }

# Configuração da ferramenta para uso no ADK
document_fetcher = fetch_document_content