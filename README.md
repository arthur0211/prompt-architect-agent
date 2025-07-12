# Prompt Architect Agent

Um agente inteligente construído com Google ADK que atua como um arquiteto de prompts especialista, capaz de conduzir entrevistas estruturadas e criar prompts profissionais de alta qualidade.

## Características

🎯 **Especializado**: Focado exclusivamente em arquitetura de prompts  
🔍 **Inteligente**: Faz perguntas estratégicas para eliminar ambiguidades  
🌐 **Conectado**: Pode pesquisar informações complementares na web  
📄 **Versátil**: Lê documentos e URLs para contexto adicional  
✨ **Profissional**: Segue melhores práticas e padrões da indústria  

## Funcionalidades

### Core
- Análise de requisitos e identificação de ambiguidades
- Entrevista estruturada com perguntas estratégicas
- Geração de prompts seguindo melhores práticas
- Formato padronizado com tags XML e markdown

### Ferramentas Integradas
- **Busca Web**: Pesquisa Google para informações complementares
- **Fetch URL**: Extração de conteúdo de URLs específicas
- **Leitura de Documentos**: Análise de arquivos locais

## Instalação

1. **Clone/baixe o projeto**
```bash
cd prompt-architect
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Configure a API Key**
Edite o arquivo `.env` e adicione sua chave:
```
GEMINI_API_KEY=sua_chave_aqui
```

## Uso

### Interface Visual (Recomendado)
```bash
adk web
```

### Interface Terminal
```bash
adk run
```

### Teste da Configuração
```bash
python agent.py
```

## Como Funciona

1. **Análise Inicial**: O agente analisa sua descrição inicial
2. **Entrevista**: Faz perguntas estratégicas sobre:
   - Contexto e objetivo
   - Requisitos técnicos  
   - Qualidade e validação
   - Necessidades de pesquisa
3. **Pesquisa**: Busca informações complementares quando necessário
4. **Geração**: Cria prompt estruturado com tags XML

## Exemplo de Saída

```markdown
# Assistente de Análise de Dados

## Contexto
Criar um assistente especializado em análise exploratória de dados...

## Tarefa
<task>
Analisar datasets fornecidos e gerar insights acionáveis...
</task>

## Instruções
<instructions>
1. Carregue e examine a estrutura dos dados
2. Identifique padrões e anomalias
3. Gere visualizações relevantes
</instructions>

## Formato de Saída
<output_format>
- Resumo executivo
- Visualizações com insights
- Recomendações acionáveis
</output_format>
```

## Estrutura do Projeto

```
prompt-architect/
├── agent.py              # Agente principal
├── tools/                # Ferramentas customizadas
│   ├── web_search.py     # Busca na web
│   ├── url_fetcher.py    # Fetch de URLs
│   └── document_fetcher.py # Leitura de documentos
├── requirements.txt      # Dependências
├── .env                 # Configurações
└── README.md           # Este arquivo
```

## Configuração da API Key

Obtenha sua chave da API do Gemini:
1. Acesse [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Crie uma nova API key
3. Adicione no arquivo `.env`

## Suporte

Para dúvidas e problemas, verifique:
- Se a API key está corretamente configurada
- Se todas as dependências foram instaladas
- Se está usando Python 3.9+