# 📐 Arquitetura do Sistema | Tikin

Este documento descreve a arquitetura de software, o fluxo de dados e os módulos funcionais do assistente financeiro **Tikin**.

---

## 🔄 Fluxo de Dados Ponta a Ponta

O fluxo de comunicação e processamento de uma solicitação no Tikin segue o diagrama abaixo:

```text
[ Usuário ]
    │
    │ 1. Interage via Chat / Botão Rápido
    ▼
[ Streamlit UI (app.py) ]
    │
    │ 2. Envia o histórico de mensagens da sessão
    ▼
[ AgenteTikin (src/agente.py) ]
    │
    │ 3. Solicita o System Prompt consolidado
    ▼
[ System Prompt & Context Injection (src/prompts.py + src/dados.py) ]
    │
    │ 4. Lê os 5 arquivos de dados locais em data/ e monta o System Prompt
    ▼
[ Gemini API — google-genai SDK ] (modelo: gemini-3.6-flash)
    │
    │ 5. Processa a instrução de sistema + histórico e gera a resposta
    ▼
[ AgenteTikin (src/agente.py) ]
    │
    │ 6. Trata potenciais exceções e retorna a resposta formatada
    ▼
[ Streamlit UI (app.py) ]
    │
    │ 7. Exibe a resposta ao usuário sem ícones de âncora (anchors=False)
    ▼
[ Usuário ]
```

---

## 🧩 Componentes do Sistema e Responsabilidades

### 1. Camada de Apresentação ([`app.py`](../app.py))
- Desenvolvida em **Streamlit**.
- Gerencia o estado da sessão (`st.session_state.messages`).
- Renderiza a barra lateral com o perfil do cliente João Silva, dicas de segurança e campo para chave de API.
- Apresenta botões de atalhos rápidos de perguntas.
- Formata a renderização de Markdown desativando âncoras automáticas de títulos (`anchors=False` e CSS `.header-anchor`).

### 2. Camada de Orquestração do Agente ([`src/agente.py`](../src/agente.py))
- Classe `AgenteTikin`.
- Utiliza o SDK oficial `google-genai`.
- Converte o histórico da conversa para o formato `types.Content` e `types.Part`.
- Define os parâmetros de geração (`types.GenerateContentConfig`) usando `system_instruction`, `temperature=0.7` e `max_output_tokens=2048`.
- Trata exceções da API de forma segura, evitando vazamento de stack traces ou credenciais.

### 3. Camada de Engenharia de Prompt e Contexto ([`src/prompts.py`](../src/prompts.py))
- Função `obter_system_prompt()`.
- Combina as diretrizes de comportamento do assistente (persona, sigilo de dados, defesa contra prompt injection, guardrails de aconselhamento) com a base de dados do cliente.
- Aplica a técnica de **Context Injection**.

### 4. Camada de Acesso aos Dados Locais ([`src/dados.py`](../src/dados.py))
- Lê os arquivos locais da pasta `data/`:
  - `perfil_investidor.json`
  - `transacoes.csv`
  - `produtos_financeiros.json`
  - `historico_atendimento.csv`
  - `seguranca_digital.json`
- Formata os dados em estruturas de texto legíveis e estruturadas para injeção no modelo.

### 5. Camada de Configurações ([`src/config.py`](../src/config.py))
- Gerencia o carregamento de variáveis de ambiente (`.env`).
- Define as constantes globais do modelo (`MODEL_NAME = "gemini-3.6-flash"`, `TEMPERATURE = 0.7`, `MAX_OUTPUT_TOKENS = 2048`).
- Fornece funções de validação da `GEMINI_API_KEY`.

---

## 💡 Decisão de Projeto: Context Injection Puro (Sem RAG / Sem Banco Vetorial)

Para o escopo do desafio e a volumetria da base do cliente, a arquitetura optou por **Context Injection Direto** no System Prompt em vez de um sistema RAG (Retrieval-Augmented Generation) com embeddings e banco vetorial:

- **Vantagens da Escolha**:
  1. **Determinismo**: Todos os dados do perfil, extrato e produtos são garantidamente apresentados ao modelo em cada chamada.
  2. **Menor Latência e Complexidade**: Elimina etapas de chunking, geração de embeddings e buscas vetoriais em bancos externos.
  3. **Custo e Simplicidade**: Reduz o número de dependências de software e chamadas adicionais à API.
