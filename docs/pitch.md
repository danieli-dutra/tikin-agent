# 📢 Pitch de Apresentação | Tikin

> **Tikin: um assistente financeiro inteligente que ajuda a cuidar do bolso e da segurança digital.**

---

## 🎯 O desafio

A ideia do Tikin nasceu de uma percepção simples: lidar com dinheiro no dia a dia já pode ser complicado, e fazer isso com segurança em um ambiente cada vez mais digital adiciona outra camada de preocupação.

O cliente precisa entender para onde o dinheiro está indo, tomar decisões financeiras mais conscientes e, ao mesmo tempo, reconhecer situações que podem colocar seus dados e seu dinheiro em risco.

Foi pensando nessa combinação que surgiu o Tikin.

---

## 💡 A solução

O **Tikin** é um assistente financeiro pessoal construído com **Python**, **Streamlit** e a **API do Gemini**, utilizando o SDK oficial `google-genai`.

A proposta não é simplesmente entregar números ou respostas prontas. O Tikin usa o contexto do cliente para transformar dados financeiros em uma conversa mais clara e próxima.

Ele pode:

- **Analisar despesas** e apresentar os gastos de forma simples;
- **Orientar sobre investimentos** considerando o perfil e os objetivos do cliente;
- **Ajudar na organização financeira**, especialmente em relação à reserva de emergência;
- **Orientar sobre segurança digital**, explicando como reconhecer golpes e situações de engenharia social.

---

## 🧠 Como o Tikin funciona

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

O projeto incorpora **guardrails no System Prompt** para:

- reduzir riscos de *Prompt Injection*;
- impedir solicitações de senhas, CVVs, tokens e códigos SMS;
- evitar exposição da `GEMINI_API_KEY`;
- restringir o assistente ao seu escopo financeiro e de segurança digital;
- tratar erros da API sem expor informações sensíveis.

A preocupação aqui foi construir não apenas um assistente que responde, mas um assistente que também sabe **o que não deve pedir ou revelar**.

---

## 🚀 Diferenciais da solução

### 1. Contexto antes de resposta

O Tikin não recebe apenas uma pergunta isolada. Ele recebe o contexto necessário para compreender o cenário daquele cliente.

### 2. Finanças + segurança digital

A proposta une dois problemas que fazem parte da mesma experiência bancária: cuidar do dinheiro e saber protegê-lo.

### 3. Vibe Coding com responsabilidade

O projeto foi desenvolvido utilizando IA como parte do processo de construção, mas com preocupação em validar código, testar funcionalidades, documentar decisões e aplicar princípios de segurança.

### 4. Interface simples e conversacional

A interface em Streamlit foi pensada para reduzir a barreira entre o usuário e as informações financeiras, utilizando conversa e atalhos rápidos em vez de exigir que o cliente saiba exatamente onde procurar cada informação.

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

## 🎤 Por que Tikin?

O nome e a proposta representam uma ideia que guiou o projeto desde o começo: **tornar uma relação que muitas vezes é complicada mais simples e mais humana**.

A tecnologia aqui não é o objetivo final.

Ela é o meio para transformar dados, contexto e inteligência artificial em uma experiência que ajude o cliente a entender melhor suas próprias decisões financeiras e a navegar pelo ambiente digital com mais segurança.

Esse é o Tikin.
