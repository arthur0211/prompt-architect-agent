import requests
from bs4 import BeautifulSoup
import urllib.parse

def web_search(query: str, num_results: int = 5) -> dict:
    """Realiza uma busca na web usando DuckDuckGo e retorna os resultados.
    
    Use esta ferramenta para buscar informações gerais, melhores práticas, 
    exemplos de prompts similares ou qualquer informação relevante.
    
    Args:
        query: Termo de busca ou pergunta
        num_results: Número de resultados a retornar (padrão: 5, máximo: 10)
        
    Returns:
        Dicionário com 'status', 'query', 'results' (lista) ou 'error'
    """
    try:
        # Validar entrada
        if not query or not isinstance(query, str):
            raise ValueError("Query deve ser uma string válida")
        
        if num_results < 1 or num_results > 10:
            num_results = 5
        
        # Usar DuckDuckGo para busca (não requer API key)
        encoded_query = urllib.parse.quote_plus(query)
        url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extrair resultados
        results = []
        result_links = soup.find_all('a', class_='result__a')
        
        for i, link in enumerate(result_links[:num_results]):
            try:
                title = link.get_text(strip=True)
                href = link.get('href')
                
                # Pegar snippet do resultado
                result_div = link.find_parent('div', class_='result')
                snippet = ""
                if result_div:
                    snippet_elem = result_div.find('a', class_='result__snippet')
                    if snippet_elem:
                        snippet = snippet_elem.get_text(strip=True)
                
                if title and href:
                    results.append({
                        "title": title,
                        "url": href,
                        "snippet": snippet,
                        "position": i + 1
                    })
            except Exception:
                continue
        
        return {
            "status": "success",
            "query": query,
            "results": results,
            "total_results": len(results)
        }
        
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "query": query,
            "error": f"Erro de rede: {str(e)}",
            "error_type": "network_error"
        }
    except ValueError as e:
        return {
            "status": "error",
            "query": query,
            "error": f"Erro de validação: {str(e)}",
            "error_type": "validation_error"
        }
    except Exception as e:
        return {
            "status": "error",
            "query": query,
            "error": f"Erro inesperado: {str(e)}",
            "error_type": "unexpected_error"
        }