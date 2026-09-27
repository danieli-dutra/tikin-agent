# 💰 Tikin | Assistente Financeiro Inteligente & Segurança Digital

O **Tikin** é um assistente financeiro pessoal inteligente construído com **Python**, **Streamlit** e a **API do Gemini** (via o SDK oficial `google-genai`). 

Projetado como solução para o desafio da **DIO**, o Tikin combina **Context Injection (Injeção de Contexto)** com **guardrails de segurança digital** para oferecer orientação financeira personalizada, análise de despesas, sugestões de investimento e proteção contra golpes cibernéticos.

---

## 🎯 Objetivo do Projeto

Capacitar o cliente bancário a tomar melhores decisões financeiras e proteger-se contra fraudes digitais através de uma interface de conversa simples, empática e contextualizada.

---

## 💡 Problema que Resolve

1. **Falta de visibilidade financeira clara**: Dificuldade em analisar gastos mensais categorizados e identificar oportunidades de economia.
2. **Dúvida na escolha de investimentos**: Incerteza sobre qual produto financeiro se adequa ao perfil de risco e aos objetivos pessoais (ex: construção de reserva de emergência).
3. **Vulnerabilidade a golpes digitais**: Exposição crescente a engenharia social, Golpe do Pix, falso funcionário de banco, boletos adulterados e phishing por SMS/e-mail.

---

## 👤 Público-Alvo

Clientes bancários (representados no projeto pelo perfil de **João Silva**, Analista de Sistemas de perfil moderado) que buscam:
- Organizar seu orçamento mensal;
- Construir ou validar sua reserva de emergência;
- Entender opções de renda fixa e multimercado;
- Tirar dúvidas sobre segurança bancária e prevenção de fraudes.

---

## 🚀 Funcionalidades Implementadas

- **💬 Chat Financeiro Interativo**: Interface gráfica completa desenvolvida em Streamlit.
- **📊 Análise Personalizada de Despesas**: Leitura e interpretação dos gastos recentes de Outubro.
- **📈 Recomendação de Investimentos**: Sugestões de produtos (Tesouro Selic, CDB Liquidez Diária, Fundo Multimercado Moderado, Tesouro IPCA+) alinhadas ao perfil moderado do cliente.
- **🛡️ Orientação de Segurança Digital**: Respostas e dicas preventivas contra golpes comuns e engenharia social.
- **👤 Painel Lateral do Cliente**: Exibição dos dados do perfil (Renda, Patrimônio, Reserva Atual, Objetivo) e status da API Key.
- **💡 Atalhos de Perguntas Rápidas**: Botões de um clique para consultas frequentes.
- **🗑️ Gerenciamento de Sessão**: Opção para limpar a conversa e reiniciar o atendimento.

---

## 🏛️ Arquitetura e Tecnologias

### Tecnologias Utilizadas
- **Linguagem**: Python 3.10+
- **Interface Web**: Streamlit
- **SDK LLM**: `google-genai` (SDK oficial do Google GenAI)
- **Modelo de IA**: `gemini-3.6-flash`
- **Manipulação de Dados**: Pandas
- **Configuração de Ambiente**: Python-Dotenv
- **Testes Automatizados**: Unittest (com suporte a Mocks)

### Estratégia de Context Injection (Sem RAG / Sem Banco Vetorial)
O Tikin adota a abordagem de **Context Injection Puro**:
Os 5 arquivos de dados locais em formato JSON e CSV são lidos em tempo de execução por `src/dados.py` e formatados em uma estrutura de texto legível. Essa estrutura é injetada diretamente no `system_instruction` do Gemini durante a inicialização do agente.

```text
[Arquivos Locais (JSON/CSV)] ➡️ [dados.py] ➡️ [System Prompt (prompts.py)] ➡️ [Gemini API (agente.py)]
```

---

## 📁 Estrutura do Projeto

```text
Tikin/
├── app.py                      # Aplicação principal Streamlit
├── requirements.txt            # Dependências do projeto
├── .env.example                # Template de variáveis de ambiente
├── .gitignore                  # Arquivos ignorados pelo Git
├── .vscode/
│   └── settings.json           # Configuração de paths do Pylance
├── data/                       # Base de dados local do cliente
│   ├── perfil_investidor.json
│   ├── transacoes.csv
│   ├── produtos_financeiros.json
│   ├── historico_atendimento.csv
│   └── seguranca_digital.json
├── docs/                       # Documentação detalhada
│   ├── arquitetura.md
│   ├── agente-e-prompts.md
│   ├── seguranca.md
│   ├── testes-e-metricas.md
│   └── pitch.md
│   
├── src/                        # Código-fonte dos módulos
│   ├── __init__.py
│   ├── config.py
│   ├── dados.py
│   ├── prompts.py
│   └── agente.py
└── tests/                      # Suíte de testes unitários
    └── test_tikin.py
```

---

## 🛠️ Como Configurar e Executar Localmente

### 1. Clonar o Repositório e Acessar a Pasta
```bash
git clone https://github.com/danieli-dutra/tikin-agent.git
cd tikin-agent
```

### 2. Ativar o Ambiente Virtual Python
No Windows:
```bash
.venv\Scripts\activate
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar a Chave da API Gemini
Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:
```env
GEMINI_API_KEY=sua_chave_real_aqui
```

### 5. Executar a Aplicação Web
```bash
streamlit run app.py
```
Acesse o endereço exibido no terminal (geralmente `http://localhost:8501`).

---

## 🧪 Como Executar os Testes Automatizados

A suíte de testes unitários roda localmente sem consumir cota da API do Gemini:

```bash
python -m unittest discover -s tests
```

**Resultado Esperado:**
```text
............
----------------------------------------------------------------------
Ran 12 tests in 0.028s

OK
```

---

## 🔐 Cuidados com a `GEMINI_API_KEY`

- **Sigilo Absoluto**: O arquivo `.env` está incluído no `.gitignore` e jamais deve ser commitado no repositório.
- **Mascaramento de Exceções**: O módulo `src/agente.py` trata erros de API sem expor o valor da chave em logs ou na tela.
- **Proteção do Cliente**: O assistente é programado via System Prompt para jamais solicitar senhas, códigos SMS, tokens ou CVVs dos usuários.

---

## ❓ Exemplos de Perguntas para o Tikin

1. *"Pode fazer uma análise rápida das minhas despesas de outubro?"*
2. *"Qual o melhor produto financeiro disponível para o meu perfil moderado?"*
3. *"Como posso me proteger do Golpe do Pix?"*
4. *"Minha reserva de emergência atual de R$ 10.000 é suficiente para a minha renda mensal?"*

---

## ⚠️ Limitações Atuais

- **Escopo Baseado no Perfil João Silva**: A base de dados local atual é estruturada para o cliente fictício cadastrado.
- **Sem Persistência de Banco de Dados Relacional**: Os históricos de conversa mantêm-se na memória de sessão do Streamlit durante a navegação.
- **Sem Integração Bancária em Tempo Real**: As transações são lidas a partir da base estática local em CSV.

---

## 📄 Documentação Adicional

Para mais detalhes sobre a implementação do projeto, consulte a pasta `docs/`:
- 📐 [Arquitetura do Sistema](docs/arquitetura.md)
- 🤖 [Agente e Prompts](docs/agente-e-prompts.md)
- 🛡️ [Diretrizes de Segurança](docs/seguranca.md)
- 🧪 [Testes e Métricas](docs/testes-e-metricas.md)
- 📢 [Pitch de Apresentação](docs/pitch.md)
