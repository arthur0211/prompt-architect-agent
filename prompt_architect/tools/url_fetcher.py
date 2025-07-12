import requests
from bs4 import BeautifulSoup

def fetch_url_content(url: str) -> dict:
    """Busca e extrai o conteúdo de texto de uma URL específica para incluir no contexto.
    
    Use esta ferramenta quando o usuário fornecer uma URL específica e quiser analisar
    seu conteúdo para criar prompts baseados nessa informação.
    
    Args:
        url: URL completa para buscar o conteúdo (ex: https://example.com/page)
        
    Returns:
        Dicionário com 'status' ('success' ou 'error'), 'url' e 'content' ou 'error'
    """
    try:
        # Validate URL format
        if not url or not isinstance(url, str):
            raise ValueError("URL deve ser uma string válida")
        
        if not (url.startswith('http://') or url.startswith('https://')):
            raise ValueError("URL deve começar com http:// ou https://")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove scripts e styles
        for script in soup(["script", "style"]):
            script.decompose()
            
        text = soup.get_text()
        # Limpar texto
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        content = ' '.join(chunk for chunk in chunks if chunk)
        
        # Limitar tamanho do conteúdo para evitar problemas de contexto
        max_length = 50000  # Aproximadamente 50KB
        if len(content) > max_length:
            content = content[:max_length] + "\n[...conteúdo truncado...]"
            
        return {
            "status": "success",
            "url": url,
            "content": content,
            "content_length": len(content)
        }
        
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "url": url,
            "error": f"Erro de rede: {str(e)}",
            "error_type": "network_error"
        }
    except ValueError as e:
        return {
            "status": "error",
            "url": url,
            "error": f"Erro de validação: {str(e)}",
            "error_type": "validation_error"
        }
    except Exception as e:
        return {
            "status": "error",
            "url": url,
            "error": f"Erro inesperado: {str(e)}",
            "error_type": "unexpected_error"
        }