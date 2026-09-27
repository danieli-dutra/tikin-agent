# 📢 Pitch de Apresentação | Tikin

> **Tikin: um assistente financeiro inteligente para cuidar do bolso e da segurança digital, um tikin de cada vez.**

---

## 🎯 O desafio

A ideia do Tikin nasceu de uma percepção simples: **lidar com dinheiro no dia a dia pode ser complicado.**

Entender para onde o dinheiro está indo, decidir o que fazer com o que sobra, pensar em investimentos e ainda se proteger de golpes digitais são desafios que fazem parte da vida financeira de muita gente.

E nem sempre o problema é falta de informação.

Às vezes, é justamente o excesso dela.

Foi pensando nisso que surgiu o Tikin: uma forma de transformar dados financeiros e inteligência artificial em uma conversa mais simples, contextualizada e próxima do cliente.

---

## 💡 A solução

O **Tikin** é um assistente financeiro pessoal construído com **Python**, **Streamlit** e a **API do Gemini**, utilizando o SDK oficial `google-genai`.

A proposta não é simplesmente entregar números ou respostas prontas.

O Tikin recebe o contexto do cliente e usa essas informações para transformar dados em uma conversa que faça sentido para aquela pessoa.

Ele pode:

- **📊 Analisar despesas** e mostrar de forma mais clara para onde o dinheiro está indo;
- **📈 Orientar sobre investimentos** considerando o perfil e os objetivos do cliente;
- **💰 Apoiar a organização financeira**, incluindo questões relacionadas à reserva de emergência;
- **🛡️ Orientar sobre segurança digital**, ajudando a reconhecer golpes e situações de engenharia social.

---

## 🧠 Contexto antes da resposta

Uma das decisões técnicas do projeto foi utilizar **Context Injection Puro**, sem RAG ou banco vetorial.

Os dados do cliente, transações, produtos financeiros, histórico de atendimento e informações de segurança são carregados localmente e incorporados ao contexto enviado ao modelo.

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

Essa abordagem foi escolhida porque atende ao escopo do desafio de forma simples, transparente e suficiente para o cenário proposto.

---

## 🛡️ Segurança desde o início

Como o Tikin trabalha com informações financeiras, segurança não poderia ser tratada como um detalhe.

Ela faz parte da própria construção do assistente.

O projeto incorpora **guardrails no System Prompt** para:

- reduzir riscos de *Prompt Injection*;
- impedir solicitações de senhas, CVVs, tokens e códigos SMS;
- evitar exposição da `GEMINI_API_KEY`;
- restringir o assistente ao seu escopo financeiro e de segurança digital;
- tratar erros da API sem expor informações sensíveis.

A preocupação foi construir um assistente que não apenas sabe **o que responder**, mas também **o que não deve pedir ou revelar**.

---

## 🚀 O que torna o Tikin diferente?

### 1. Contexto antes de resposta

O Tikin não recebe apenas uma pergunta isolada.

Ele recebe informações sobre o cliente, seus objetivos, transações e contexto para produzir respostas mais relevantes para aquele cenário.

### 2. Finanças + segurança digital

Cuidar do dinheiro também significa saber protegê-lo.

Por isso, o Tikin combina orientação financeira com educação sobre golpes, phishing, engenharia social e segurança bancária.

### 3. Vibe Coding com responsabilidade

A inteligência artificial fez parte do processo de desenvolvimento, mas não substituiu a validação.

O projeto foi construído com revisão de código, testes automatizados, documentação das decisões técnicas e preocupação com segurança.

### 4. Uma experiência simples e conversacional

Em vez de obrigar o usuário a descobrir onde encontrar cada informação, o Tikin coloca a conversa no centro da experiência.

A ideia é diminuir a distância entre **“eu tenho uma dúvida”** e **“agora eu entendi o que está acontecendo”.**

---

## 🧪 Validação

O projeto possui uma suíte automatizada com **12 testes unitários**, cobrindo os principais módulos da aplicação.

Resultado da última execução local:

```text
............
----------------------------------------------------------------------
Ran 12 tests in 0.028s

OK
```

Além dos testes, a aplicação também foi validada quanto à importação do `app.py` e à organização da estrutura do projeto.

---

## ✨ Por que Tikin?

O nome nasceu de uma ideia simples:

> **ajudar a pessoa a entender melhor seu dinheiro, um tikin de cada vez.**

Porque cuidar da vida financeira não precisa começar com uma grande mudança.

Pode começar entendendo um gasto.

Organizando uma escolha.

Criando uma pequena reserva.

Ou simplesmente fazendo uma pergunta.

**Um tikin de cada vez.**

Esse conceito acabou guiando não apenas o nome, mas também a proposta do produto: tornar uma relação que muitas vezes parece complicada mais simples, próxima e compreensível.

---

## 💜 O que o Tikin representa

Para mim, tecnologia não deveria ser o objetivo final.

Ela é o meio.

O objetivo é transformar dados, contexto e inteligência artificial em uma experiência que ajude o cliente a entender melhor suas próprias decisões financeiras e a navegar pelo ambiente digital com mais segurança.

O Tikin nasceu de uma ideia pequena, mas com uma proposta muito prática:

**ajudar a cuidar do dinheiro, um tikin de cada vez.**
