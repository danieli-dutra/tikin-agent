# 💰 Tikin | Assistente Financeiro Inteligente & Segurança Digital

> **Um tikin daqui, outro tikin dali. No fim, faz diferença.**

O **Tikin** é um assistente financeiro pessoal inteligente construído com **Python**, **Streamlit** e a **API do Gemini**, utilizando o SDK oficial `google-genai`.

O nome Tikin nasceu de uma ideia simples e bem brasileira: guardar **um tikin daqui, outro tikin dali**. Pequenas decisões financeiras, quando entendidas e acompanhadas ao longo do tempo, podem fazer diferença.

Desenvolvido como solução para um desafio da **DIO**, o projeto combina **Context Injection**, inteligência artificial e **guardrails de segurança digital** para criar uma experiência de orientação financeira mais clara, contextualizada e próxima do usuário.

---

## 🎯 A ideia por trás do projeto

Dinheiro costuma envolver duas coisas que nem sempre andam juntas: **informação e tranquilidade**.

É fácil olhar para uma lista de gastos e não saber o que fazer com ela. Também é comum ter dúvidas sobre investimentos, reserva de emergência ou sobre como reconhecer uma tentativa de golpe.

A proposta do Tikin é transformar esses dados e dúvidas em uma conversa mais simples.

Em vez de apenas apresentar informações, o assistente utiliza o contexto disponível do cliente para ajudar a interpretar sua situação financeira e orientar suas próximas decisões.

---

## 💡 O problema que o Tikin aborda

O projeto foi pensado em torno de três situações:

1. **Falta de clareza sobre os próprios gastos**  
   Dificuldade para entender para onde o dinheiro está indo e identificar oportunidades de organização.

2. **Dúvidas sobre investimentos**  
   Incerteza sobre quais produtos podem fazer sentido considerando perfil de risco e objetivos financeiros.

3. **Vulnerabilidade a golpes digitais**  
   Situações como phishing, falso funcionário de banco, golpes envolvendo Pix e outras formas de engenharia social exigem informação e atenção.

O Tikin conecta esses três pontos em uma única experiência conversacional.

---

## 👤 Público-alvo

O projeto utiliza como referência um cliente fictício, **João Silva**, Analista de Sistemas com perfil de investidor moderado.

A experiência foi pensada para pessoas que querem:

- Organizar melhor o orçamento;
- Entender seus gastos;
- Construir ou acompanhar uma reserva de emergência;
- Conhecer opções de renda fixa e multimercado;
- Tirar dúvidas sobre segurança bancária;
- Reconhecer situações potencialmente fraudulentas.

---

## 🚀 Funcionalidades implementadas

- **💬 Chat financeiro interativo** — interface conversacional desenvolvida em Streamlit.
- **📊 Análise personalizada de despesas** — leitura e interpretação dos gastos recentes de outubro.
- **📈 Orientação sobre investimentos** — informações sobre produtos como Tesouro Selic, CDB com liquidez diária, Fundo Multimercado Moderado e Tesouro IPCA+, considerando o perfil do cliente fictício.
- **🛡️ Orientação de segurança digital** — dicas preventivas contra golpes e engenharia social.
- **👤 Painel do cliente** — exibição de informações do perfil, como renda, patrimônio, reserva atual e objetivo.
- **💡 Atalhos de perguntas rápidas** — acesso facilitado a consultas frequentes.
- **🗑️ Gerenciamento de sessão** — possibilidade de limpar a conversa e iniciar um novo atendimento.

---

## 🧠 Como o Tikin funciona

Uma das principais decisões técnicas do projeto foi utilizar **Context Injection Puro**, sem RAG ou banco vetorial.

Os dados disponíveis no projeto são carregados localmente por `src/dados.py`, organizados e incorporados ao contexto enviado ao modelo.

Isso permite que o Gemini receba informações sobre o cliente, suas transações, produtos financeiros, histórico de atendimento e orientações de segurança antes de responder.

```text
[Dados locais]
      ↓
[dados.py]
      ↓
[System Prompt + Guardrails]
      ↓
[Gemini API]
      ↓
[Resposta contextualizada]
```

A escolha foi intencional: para o escopo do desafio, essa abordagem mantém a arquitetura simples, transparente e fácil de compreender.

---

## 🛡️ Segurança desde o início

Como o Tikin trabalha com informações financeiras, segurança faz parte da própria arquitetura da solução.

O projeto utiliza **guardrails no System Prompt** para:

- Reduzir riscos de *Prompt Injection*;
- Impedir solicitações de senhas, CVVs, tokens e códigos SMS;
- Evitar exposição da `GEMINI_API_KEY`;
- Restringir o assistente ao escopo financeiro e de segurança digital;
- Tratar erros da API sem expor informações sensíveis.

A preocupação não foi apenas fazer o assistente responder bem, mas também definir **o que ele não deve pedir, revelar ou fazer**.

---

## 🏛️ Tecnologias utilizadas

- **Python 3.10+**
- **Streamlit**
- **Google GenAI SDK (`google-genai`)**
- **Gemini**
- **Pandas**
- **Python-Dotenv**
- **Unittest + Mocks**

---

## 🧪 Validação

O projeto possui uma suíte de **12 testes unitários**, cobrindo os principais módulos da aplicação.

Resultado da execução local:

```text
............
----------------------------------------------------------------------
Ran 12 tests in 0.028s

OK
```

A aplicação também foi validada quanto à importação do `app.py` e à organização da estrutura do projeto.

---

## 📁 Estrutura do projeto

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
GEMINI_API_KEY=sua_chave_aqui
```

> A chave não deve ser commitada. O arquivo `.env` está protegido pelo `.gitignore`.

### 5. Executar a aplicação

```bash
streamlit run app.py
```

Acesse o endereço exibido pelo Streamlit, normalmente:

```text
http://localhost:8501
```

---

## 🔐 Cuidados com a `GEMINI_API_KEY`

- O arquivo `.env` está incluído no `.gitignore`.
- A chave não é armazenada no código-fonte.
- Os erros da API são tratados sem expor informações sensíveis.
- O assistente possui instruções para não solicitar senhas, CVVs, tokens ou códigos SMS.

---

## ❓ Exemplos de perguntas

```text
"Pode fazer uma análise rápida das minhas despesas de outubro?"

"Quais opções de investimento fazem sentido para o meu perfil moderado?"

"Como posso me proteger do Golpe do Pix?"

"Minha reserva de emergência atual é suficiente para a minha renda?"
```

---

## ⚠️ Limitações atuais

O Tikin é um projeto desenvolvido para um cenário controlado e possui algumas limitações:

- **Perfil fictício:** os dados atuais são estruturados para o cliente de demonstração João Silva.
- **Sem banco de dados relacional:** o histórico da conversa permanece na memória da sessão do Streamlit.
- **Sem integração bancária em tempo real:** as transações utilizadas pelo assistente vêm de uma base local em CSV.
- **Sem recomendação financeira automatizada para clientes reais:** as orientações apresentadas fazem parte do cenário demonstrativo do projeto.

---

## 📚 Documentação

A pasta `docs/` contém a documentação complementar do projeto:

- 📐 [Arquitetura do Sistema](docs/arquitetura.md)
- 🤖 [Agente e Prompts](docs/agente-e-prompts.md)
- 🛡️ [Diretrizes de Segurança](docs/seguranca.md)
- 🧪 [Testes e Métricas](docs/testes-e-metricas.md)
- 📢 [Pitch de Apresentação](docs/pitch.md)

---

## 👩‍💻 Sobre o projeto

O Tikin nasceu como um desafio técnico, mas acabou se tornando também um exercício de produto.

A intenção foi juntar algumas coisas que fazem sentido para mim: **tecnologia, experiência do usuário, inteligência artificial e resolução de problemas reais**.

Durante o desenvolvimento, a preocupação não ficou apenas em fazer a aplicação funcionar. Também entraram na conta arquitetura, segurança, testes, documentação e, principalmente, a experiência de quem estaria do outro lado da tela.

No fim, a ideia continua sendo a mesma do nome:

> **Um tikin daqui, outro tikin dali. Pequenas decisões também constroem grandes resultados.**

---
