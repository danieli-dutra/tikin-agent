# 🧪 Testes e Resultados — Tikin

Este documento apresenta a suíte de testes unitários automatizados do projeto **Tikin**, a metodologia de validação utilizada e os resultados reais de execução.

---

## 🎯 Metodologia de Testes

Os testes foram desenvolvidos utilizando o framework nativo **Unittest** da biblioteca padrão do Python. Toda a suíte foi projetada para rodar **localmente e de forma determinística**, utilizando isolamento de ambiente e objetos Mock (`unittest.mock.patch`), sem realizar chamadas reais à API do Gemini e sem consumir cota de rede.

---

## 💻 Comando de Execução dos Testes

Os testes são executados no ambiente Python do projeto (`.venv`):

```bash
python -m unittest discover -s tests
```

---

## 📊 Resultado Real da Execução

```text
............
----------------------------------------------------------------------
Ran 12 tests in 0.028s

OK
```

- **Total de Testes Executados**: 12
- **Testes Aprovados**: 12 (100%)
- **Falhas / Erros**: 0

---

## 📝 Detalhamento dos 12 Casos de Teste

### Módulo `TestConfig` ([`src/config.py`](../src/config.py))
1. **`test_paths_e_constantes`**: Valida a existência das constantes `MODEL_NAME`, `DATA_DIR` e confirma que o diretório de dados existe.
2. **`test_api_key_check`**: Valida se a função `is_api_key_configured()` retorna um valor booleano consistente.

### Módulo `TestDados` ([`src/dados.py`](../src/dados.py))
3. **`test_carregar_perfil`**: Confirma que `carregar_perfil()` lê e formata corretamente o nome ("João Silva") e o perfil ("moderado").
4. **`test_carregar_transacoes`**: Confirma que `carregar_transacoes()` lê os lançamentos de outubro ("Salário", "Aluguel") com formatação monetária (R$).
5. **`test_carregar_produtos`**: Confirma que `carregar_produtos()` lê as opções de renda fixa e multimercado ("Tesouro Selic", "CDB Liquidez Diária").
6. **`test_carregar_atendimentos`**: Confirma que `carregar_atendimentos()` lê os registros do histórico de suporte ("CDB", "Golpe do Pix").
7. **`test_carregar_seguranca_digital`**: Confirma que `carregar_seguranca_digital()` inclui as seções de golpes comuns, boas práticas e itens proibidos.
8. **`test_carregar_todo_contexto`**: Valida a consolidação completa das 5 seções no contexto formatado final.

### Módulo `TestPrompts` ([`src/prompts.py`](../src/prompts.py))
9. **`test_obter_system_prompt`**: Confirma que `obter_system_prompt()` inclui o nome do assistente ("Tikin"), as regras de segurança e privacidade, a defesa contra prompt injection e os dados do cliente.

### Módulo `TestAgente` ([`src/agente.py`](../src/agente.py))
10. **`test_resposta_sem_api_key`**: Verifica se `AgenteTikin(api_key="")` retorna o aviso seguro solicitando a configuração da chave sem tentar conexões externas.
11. **`test_resposta_sucesso_mock`**: Valida a geração de resposta utilizando um mock do `genai.Client` para simular retorno com sucesso da API.
12. **`test_tratamento_erro_api_key_invalida`**: Valida o tratamento seguro de exceção da API (mock de erro `API_KEY_INVALID`), confirmando que a mensagem amigável é retornada ao usuário sem vazar exceções puras.

---

## 📌 Nota sobre Métricas

Nenhuma métrica sintética não medida (como porcentagens inventadas de "acurácia estatística" ou "precisão de linguagem") foi incluída neste relatório. Os resultados apresentados refletem **estritamente a execução real da suíte de testes unitários do repositório**.
