# 💰 Tikin | Assistente Financeiro Inteligente & Segurança Digital

> **Guardar um tikin daqui, outro tikin dali. No fim, faz diferença.**

O **Tikin** é um assistente financeiro pessoal inteligente construído para o desafio da DIO. A proposta nasceu de uma ideia simples: tornar a relação com dinheiro um pouco mais clara, prática e humana, usando **Python**, **Streamlit** e a **API do Gemini** por meio do SDK oficial `google-genai`.

O nome vem justamente dessa ideia de juntar pequenos valores ao longo do tempo. Um **tikin daqui, outro tikin dali** pode se transformar em uma reserva, em uma meta ou simplesmente em uma relação mais consciente com o próprio dinheiro.

Além da organização financeira, o Tikin também aborda **segurança digital**, porque cuidar do dinheiro em um ambiente cada vez mais digital também significa saber reconhecer golpes e proteger informações pessoais.

---

## 🎯 O desafio

O desafio da DIO propõe a criação de um **Assistente Virtual com Inteligência Artificial** capaz de conversar com uma pessoa usuária, entender uma necessidade e responder com base em informações organizadas.

A partir dessa proposta, o Tikin foi construído com foco em três necessidades:

1. **Entender melhor os próprios gastos** e identificar oportunidades de organização;
2. **Receber orientação financeira contextualizada**, considerando perfil e objetivos;
3. **Reconhecer situações de risco digital**, como golpes e tentativas de engenharia social.

A ideia não foi criar uma solução financeira completa, mas um protótipo funcional que demonstrasse como IA, contexto e uma base de conhecimento podem ser combinados em uma experiência conversacional.

---

## 💡 A solução

O Tikin funciona como um assistente conversacional que recebe uma pergunta e utiliza o contexto disponível sobre o cliente para construir a resposta.

No cenário desenvolvido para o projeto, o cliente fictício **João Silva**, Analista de Sistemas com perfil moderado, possui dados de renda, patrimônio, reserva financeira, transações, produtos disponíveis, histórico de atendimento e informações relacionadas à segurança digital.

Com esse contexto, o Tikin pode:

- 💬 Conversar sobre questões financeiras;
- 📊 Analisar despesas e apresentar os gastos de forma simples;
- 📈 Orientar sobre produtos financeiros considerando perfil e objetivos;
- 💰 Ajudar na organização e no planejamento da reserva de emergência;
- 🛡️ Explicar como reconhecer golpes e situações de engenharia social;
- ❓ Informar quando uma resposta não está contemplada pelo contexto disponível.

---

## 🧠 Como o Tikin funciona

Uma das principais decisões técnicas do projeto foi utilizar **Context Injection Puro**, sem RAG ou banco vetorial.

Os dados locais são carregados em tempo de execução pelo módulo `src/dados.py`. Depois, são organizados em uma estrutura de contexto que é incorporada às instruções do agente antes da chamada ao Gemini.

```text
[Dados locais]
      ↓
[src/dados.py]
      ↓
[System Prompt + Guardrails]
      ↓
[Gemini API]
      ↓
[Resposta contextualizada]
```

A abordagem foi escolhida por ser adequada ao escopo do desafio: simples de implementar, fácil de entender e suficiente para trabalhar com a pequena base de conhecimento utilizada pelo protótipo.

---

## 🛡️ Segurança desde o início

Como o Tikin trabalha com informações financeiras, segurança foi considerada parte da solução desde a construção do agente.

O projeto utiliza **guardrails no System Prompt** para estabelecer limites de comportamento, incluindo:

- redução de riscos relacionados a *Prompt Injection*;
- proteção contra exposição da `GEMINI_API_KEY`;
- proibição de solicitar senhas, CVVs, tokens e códigos SMS;
- restrição do agente ao contexto financeiro e de segurança digital;
- tratamento de erros da API sem expor informações sensíveis.

A ideia é que o assistente não apenas saiba responder, mas também saiba **o que não deve pedir, revelar ou inventar**.

---

## 🚀 Funcionalidades implementadas

- **💬 Chat Financeiro Interativo**  
  Interface conversacional desenvolvida com Streamlit.

- **📊 Análise Personalizada de Despesas**  
  Leitura e interpretação das transações disponíveis na base local.

- **📈 Orientação sobre Investimentos**  
  Contextualização de produtos financeiros de acordo com o perfil e objetivo do cliente fictício.

- **🛡️ Orientação de Segurança Digital**  
  Informações preventivas sobre golpes comuns e engenharia social.

- **👤 Painel do Cliente**  
  Exibição de informações do perfil utilizado no cenário do projeto.

- **💡 Perguntas Rápidas**  
  Atalhos para facilitar a exploração das principais funcionalidades.

- **🗑️ Gerenciamento de Sessão**  
  Possibilidade de limpar a conversa e iniciar um novo atendimento.

---

## 🏛️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| **Python 3.10+** | Linguagem principal |
| **Streamlit** | Interface web |
| **Google GenAI (`google-genai`)** | Integração com o Gemini |
| **Gemini** | Modelo de IA utilizado pelo agente |
| **Pandas** | Manipulação dos dados |
| **python-dotenv** | Gerenciamento de variáveis de ambiente |
| **Unittest + Mocks** | Testes automatizados |

---

## 📁 Estrutura do projeto

```text
tikin-agent/
├── app.py                      # Aplicação principal Streamlit
├── requirements.txt            # Dependências do projeto
├── .env.example                # Template de variáveis de ambiente
├── .gitignore                  # Arquivos ignorados pelo Git
├── .vscode/
│   └── settings.json           # Configurações do ambiente de desenvolvimento
├── data/                       # Base de conhecimento local
│   ├── perfil_investidor.json
│   ├── transacoes.csv
│   ├── produtos_financeiros.json
│   ├── historico_atendimento.csv
│   └── seguranca_digital.json
├── docs/                       # Documentação do projeto
│   ├── arquitetura.md
│   ├── agente-e-prompts.md
│   ├── seguranca.md
│   ├── testes-e-metricas.md
│   └── pitch.md
├── references/                 # Referências utilizadas no desenvolvimento
├── src/                        # Código-fonte
│   ├── __init__.py
│   ├── config.py
│   ├── dados.py
│   ├── prompts.py
│   └── agente.py
└── tests/                      # Testes automatizados
    └── test_tikin.py
```

---

## 🛠️ Como executar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/danieli-dutra/tikin-agent.git
cd tikin-agent
```

### 2. Criar e ativar o ambiente virtual

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar a API do Gemini

Crie um arquivo `.env` na raiz do projeto com base no `.env.example`:

```env
GEMINI_API_KEY=sua_chave_real_aqui
```

A chave também pode ser informada pela própria interface do Streamlit, conforme a implementação atual.

### 5. Executar a aplicação

```bash
streamlit run app.py
```

A aplicação será disponibilizada pelo endereço exibido no terminal, normalmente:

```text
http://localhost:8501
```

---

## 🧪 Testes

O projeto possui uma suíte de testes unitários para validar os principais módulos da aplicação.

Os testes podem ser executados sem consumir a cota da API do Gemini:

```bash
python -m unittest discover -s tests
```

Resultado da validação realizada durante a publicação:

```text
............
----------------------------------------------------------------------
Ran 12 tests in 0.028s

OK
```

Além dos testes automatizados, o projeto passou por uma verificação de importação do `app.py` e por uma auditoria pré-publicação do repositório.

---

## 🔐 Segurança da API Key

A `GEMINI_API_KEY` é uma credencial sensível e não faz parte do repositório.

O projeto utiliza:

- `.env` para configuração local;
- `.env.example` apenas como modelo;
- `.gitignore` para impedir o versionamento do `.env`;
- tratamento de erros para evitar exposição da chave em mensagens da aplicação.

**Nunca publique uma API Key real no GitHub.**

---

## ❓ Exemplos de perguntas

Alguns exemplos para testar o Tikin:

> "Pode fazer uma análise rápida das minhas despesas de outubro?"

> "Quais produtos financeiros estão disponíveis para o meu perfil?"

> "Como posso me proteger do Golpe do Pix?"

> "Minha reserva atual é suficiente para o meu objetivo?"

---

## ⚠️ Limitações atuais

O Tikin é um **protótipo desenvolvido para um desafio educacional**. Algumas limitações fazem parte do escopo atual:

- A base de conhecimento utiliza um cliente fictício;
- Os dados financeiros são estáticos e armazenados localmente;
- Não existe integração com uma conta bancária real;
- Não há persistência de conversas em banco de dados;
- O Context Injection é adequado para a pequena quantidade de dados do projeto, mas não necessariamente para bases maiores;
- As orientações financeiras são demonstrativas e não substituem aconselhamento financeiro profissional.

---

## 📚 Documentação

A pasta `docs/` contém os materiais utilizados para documentar as principais decisões do projeto:

- 📐 [Arquitetura do Sistema](docs/arquitetura.md)
- 🤖 [Agente e Prompts](docs/agente-e-prompts.md)
- 🛡️ [Diretrizes de Segurança](docs/seguranca.md)
- 🧪 [Testes e Métricas](docs/testes-e-metricas.md)
- 📢 [Pitch de Apresentação](docs/pitch.md)

---

## 👩‍💻 Sobre o projeto

O Tikin foi desenvolvido como um projeto de aprendizado e portfólio durante minha formação em **Análise e Desenvolvimento de Sistemas** e no curso de **Desenvolvimento Full Stack da +praTi/Codifica**.

Mais do que tentar criar uma aplicação financeira completa, a proposta foi experimentar na prática como transformar uma ideia em um produto funcional, passando por diferentes etapas: definição do problema, organização da base de conhecimento, construção de prompts, desenvolvimento da interface, integração com IA, testes e documentação.

Durante o desenvolvimento, a IA também fez parte do processo de construção. O objetivo, porém, foi utilizá-la como ferramenta de apoio, mantendo a preocupação em **entender o código, validar o comportamento, testar a aplicação e documentar as decisões tomadas**.

O Tikin é, acima de tudo, um exercício de colocar tecnologia para resolver um problema cotidiano de uma forma simples e próxima.

---

## 📌 Desafio

Projeto desenvolvido como parte do Lab da **Digital Innovation One (DIO)**:

**Construa Seu Assistente Virtual Com Inteligência Artificial**

A implementação apresentada neste repositório é uma adaptação própria do desafio, com identidade, contexto, arquitetura e funcionalidades definidas durante o desenvolvimento.

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e de portfólio.
