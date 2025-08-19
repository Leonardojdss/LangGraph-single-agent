# LangGraph Single Agent shorts #03

## Repositorio desenvolvido por Leonardojdss para demonstrar a criação e uso de um single-agent com ferramentas e memória

Um agente de IA inteligente construído com LangGraph que utiliza memória e ferramentas especializadas para consultas de CEP brasileiro e extração de dados web.

![Arquitetura do Projeto](image.png)

## 📋 Descrição

Este projeto demonstra a implementação de um agente de IA conversacional usando o framework LangGraph, com capacidades de:
- **Consulta de CEP**: Busca informações de endereços brasileiros via API ViaCEP
- **Extração de dados web**: Extrai dados estruturados de websites usando AgentQL
- **Memória persistente**: Mantém contexto da conversa usando InMemorySaver
- **chat no terminal**: Interface simples para interação com o agent

## 🚀 Funcionalidades

### 🔧 Ferramentas Disponíveis

1. **ToolViaCep**: Consulta endereços brasileiros por CEP
   - Busca informações completas de logradouro, bairro, cidade, UF
   - Integração com a API pública ViaCEP
   - Input: Informe um CEP

2. **ToolsAgentQL**: Extração inteligente de dados web
   - Extrai dados estruturados de qualquer website
   - Usa queries em linguagem natural para especificar dados desejados
   - input: Informe uma URL

### 💬 Interface de Chat

- Chat interativo via terminal
- Comandos de saída: `exit` ou `quit`
- Suporte a múltiplas consultas na mesma sessão
- Memória de contexto entre mensagens

## 📁 Estrutura do Projeto

```
src/
├── main.py                    # Ponto de entrada da aplicação
├── agent/
│   ├── single_agent.py        # Implementação do agente principal
│   └── utils/
│       ├── chat.py           # Interface de chat
│       └── message_template.py # Formatação de mensagens
├── infrastructure/
│   └── openai_connection.py   # Conexão com Azure OpenAI
└── tools/
    ├── tools.py              # Interface abstrata para ferramentas
    ├── tool_viacep.py        # Ferramenta de consulta CEP
    └── tool_agentql.py       # Ferramenta de extração web
```

## 🛠️ Tecnologias Utilizadas

- **LangGraph**: Framework para construção de agentes
- **LangChain**: Integração com LLMs e ferramentas
- **Azure OpenAI**: Modelo de linguagem GPT-4.1
- **AgentQL**: Extração de dados web
- **ViaCEP API**: Consulta de CEPs brasileiros
- **Python 3.12**: Linguagem de programação

## ⚙️ Configuração

### Pré-requisitos

- Python 3.12+
- Conta Azure OpenAI
- Chave API AgentQL (opcional)

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/Leonardojdss/LangGraph-single-agent.git
cd LangGraph-single-agent
```

2. **Crie e ative o ambiente virtual**
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
# ou
env\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**
Crie um arquivo `.env` na raiz do projeto:
```env
AZURE_OPENAI_DEPLOYMENT_NAME=seu-deployment-name
AZURE_OPENAI_API_KEY=sua-api-key
AZURE_OPENAI_ENDPOINT=seu-endpoint
OPENAI_API_VERSION="2025-01-01-preview"
AGENTQL_API_KEY=sua-agentql-key
```

## 🚀 Como Usar

### Configurar PYTHONPATH
```bash
export PYTHONPATH=<raiz do projeto>
```

### Executar o Chat
```bash
python src/main.py
```

### Exemplos de Uso

**Consulta de CEP:**
```
User: Qual o endereço do CEP 01001000?
```

**Extração de dados web:**
```
User: o que tem nessa página https://github.com/Leonardojdss
```

## 👨‍💻 Autor

**Leonardo José da Silva**
- GitHub: [@Leonardojdss](https://github.com/Leonardojdss)
- LinkedIn: [Leonardo José da Silva](https://www.linkedin.com/in/leonardojdss/)