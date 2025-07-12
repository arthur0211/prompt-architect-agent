from google.adk.agents import Agent
from .tools.url_fetcher import fetch_url_content
from .tools.web_search import web_search
from . import prompt
from .config import config

def create_prompt_architect_agent():
    """
    Cria e retorna o agente arquiteto de prompts configurado.
    
    Returns:
        Agent: Instância configurada do agente arquiteto de prompts
        
    Raises:
        RuntimeError: Se houver erro na configuração do agente
    """
    try:
        # Criar o agente usando configurações centralizadas
        agent = Agent(
            name=config.agent_name,
            model=config.agent_model,
            instruction=prompt.PROMPT_ARCHITECT_INSTRUCTION,
            description=config.agent_description,
            tools=[
                web_search,
                fetch_url_content
            ]
        )
        
        return agent
        
    except Exception as e:
        raise RuntimeError(f"Erro ao criar o agente: {e}")

# Expor o agente como root_agent para o ADK
try:
    root_agent = create_prompt_architect_agent()
except Exception as e:
    print(f"Erro ao inicializar o agente: {e}")
    raise

if __name__ == "__main__":
    # Teste básico do agente
    try:
        agent = create_prompt_architect_agent()
        print("SUCESSO: Prompt Architect Agent carregado com sucesso!")
        print(f"  - Nome: {agent.name}")
        print(f"  - Modelo: {config.agent_model}")
        print(f"  - Ferramentas disponíveis: {len(agent.tools)}")
    except Exception as e:
        print(f"ERRO: {e}")
        exit(1)