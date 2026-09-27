# 🛡️ Diretrizes de Segurança | Tikin

O projeto **Tikin** foi desenvolvido incorporando princípios de **Vibe Coding Seguro** inspirados no *Guia de Segurança KipperDev*. Este documento descreve as proteções implementadas no código, no tratamento de dados e nas instruções do modelo.

---

## 🔒 1. Proteção contra Prompt Injection

- **Risco**: Usuários ou mensagens maliciosas tentarem enviar instruções para que o LLM esqueça suas regras de negócio, altere sua identidade, revele o System Prompt ou execute ações indevidas.
- **Controle Aplicado**: 
  - Diretriz 3 no System Prompt (`src/prompts.py`): Instrução explícita ordenando que o modelo ignore comandos contidos na mensagem do usuário que tentem mudar sua persona ou revelar instruções internas.
  - A validação final de ferramentas e respostas permanece sob controle do código Python na aplicação.

---

## 🔑 2. Proteção de Segredos e API Keys (Segredos no Frontend/Código)

- **Risco**: Exposição da `GEMINI_API_KEY` em código-fonte, bundles públicos, histórico do Git ou logs.
- **Controles Aplicados**:
  - A chave é lida exclusivamente via variáveis de ambiente (`.env`) no backend (`src/config.py`).
  - O arquivo `.env` está explicitamente incluído no `.gitignore`.
  - A interface gráfica aceita a chave via campo protegido `st.text_input(type="password")` apenas na memória de sessão.
  - A função `_chave_valida()` em `src/agente.py` impede o envio de valores vazios ou placeholders como `sua_chave_aqui`.

---

## 🛡️ 3. Privacidade e Proteção de Dados Sensíveis do Cliente

- **Risco**: Coleta, armazenamento ou exibição de dados críticos como senhas bancárias, tokens de verificação, códigos SMS ou CVV de cartões de crédito.
- **Controles Aplicados**:
  - Diretriz 2 no System Prompt (`src/prompts.py`): Proibição absoluta de solicitar, armazenar ou exibir dados sensíveis.
  - Caso o cliente envie dados sensíveis acidentalmente no chat, o assistente possui instrução prioritária para alertar imediatamente o usuário a jamais compartilhar tais informações.

---

## 🚨 4. Tratamento Seguro de Erros (Mensagens que Vazam Dados)

- **Risco**: Exceções da API do Gemini ou erros de runtime vazarem stack traces, rotas de arquivos internas, URLs de infraestrutura ou detalhes da chave de API para o usuário final.
- **Controle Aplicado**:
  - No método `responder()` em `src/agente.py`, todas as chamadas à API são envolvidas em blocos `try/except Exception as err`.
  - As exceções são capturadas e convertidas em mensagens amigáveis e genéricas de interface (ex: *"Chave de API inválida"*, *"Limite de cota excedido"*, *"Erro ao comunicar com o serviço de IA"*), ocultando qualquer detalhe técnico do usuário.

---

## 🎯 5. Limitação de Escopo e Respostas Fora do Escopo

- **Risco**: O assistente responder a perguntas não relacionadas a finanças/segurança ou fornecer aconselhamento de investimento desalinhado com o perfil do cliente.
- **Controles Aplicados**:
  - Escopo delimitado pelas diretrizes do System Prompt.
  - As recomendações de investimento usam como base obrigatória o perfil *moderado* e o objetivo de *reserva de emergência* do cliente João Silva, contidos na base local `data/produtos_financeiros.json`.

---

## 🕵️‍♂️ 6. Orientação de Segurança contra Golpes Digitais

- **Risco**: O cliente ser vítima de engenharia social, phishing, falso funcionário de banco ou Golpe do Pix.
- **Controle Aplicado**:
  - Injeção da base `data/seguranca_digital.json` no contexto do modelo.
  - O Tikin fornece orientações preventivas claras e instrui o cliente a entrar em contato diretamente pelos canais oficiais da instituição financeira em caso de suspeita.
