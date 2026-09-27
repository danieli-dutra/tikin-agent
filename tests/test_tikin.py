"""
Testes unitários e de integração para a aplicação Tikin.
"""

import sys
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

# Adiciona diretório src ao path de execução
_SRC_DIR = Path(__file__).resolve().parent.parent / "src"
if str(_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(_SRC_DIR))

import config
import dados
import prompts
from agente import AgenteTikin


class TestConfig(unittest.TestCase):
    """Testes para o módulo de configuração (config.py)."""

    def test_paths_e_constantes(self):
        """Verifica se os caminhos e constantes essenciais foram definidos."""
        self.assertTrue(hasattr(config, "MODEL_NAME"))
        self.assertTrue(hasattr(config, "DATA_DIR"))
        self.assertTrue(config.DATA_DIR.exists())

    def test_api_key_check(self):
        """Verifica se a função de validação de API Key retorna um booleano."""
        is_configured = config.is_api_key_configured()
        self.assertIsInstance(is_configured, bool)


class TestDados(unittest.TestCase):
    """Testes para o módulo de dados (dados.py)."""

    def test_carregar_perfil(self):
        """Verifica se o perfil do investidor é carregado corretamente."""
        perfil = dados.carregar_perfil()
        self.assertIn("João Silva", perfil)
        self.assertIn("moderado", perfil)

    def test_carregar_transacoes(self):
        """Verifica se as transações financeiras são carregadas e formatadas."""
        transacoes = dados.carregar_transacoes()
        self.assertIn("Salário", transacoes)
        self.assertIn("Aluguel", transacoes)
        self.assertIn("R$", transacoes)

    def test_carregar_produtos(self):
        """Verifica se os produtos financeiros são carregados."""
        produtos = dados.carregar_produtos()
        self.assertIn("Tesouro Selic", produtos)
        self.assertIn("CDB Liquidez Diária", produtos)

    def test_carregar_atendimentos(self):
        """Verifica se o histórico de atendimento é carregado."""
        atendimentos = dados.carregar_atendimentos()
        self.assertIn("CDB", atendimentos)
        self.assertIn("Golpe do Pix", atendimentos)

    def test_carregar_seguranca_digital(self):
        """Verifica se as informações de segurança digital são carregadas."""
        seguranca = dados.carregar_seguranca_digital()
        self.assertIn("GOLPES COMUNS", seguranca)
        self.assertIn("BOAS PRÁTICAS", seguranca)
        self.assertIn("NUNCA DEVEM SER COMPARTILHADOS", seguranca)

    def test_carregar_todo_contexto(self):
        """Verifica a consolidação do contexto completo."""
        contexto = dados.carregar_todo_contexto()
        self.assertIn("=== PERFIL DO CLIENTE ===", contexto)
        self.assertIn("=== TRANSAÇÕES RECENTES ===", contexto)
        self.assertIn("=== PRODUTOS FINANCEIROS DISPONÍVEIS ===", contexto)
        self.assertIn("=== HISTÓRICO DE ATENDIMENTOS ===", contexto)
        self.assertIn("=== SEGURANÇA FINANCEIRA DIGITAL ===", contexto)


class TestPrompts(unittest.TestCase):
    """Testes para o módulo de prompts (prompts.py)."""

    def test_obter_system_prompt(self):
        """Verifica se o system prompt inclui o contexto e as regras de segurança."""
        sp = prompts.obter_system_prompt()
        self.assertIn("Tikin", sp)
        self.assertIn("PROTEÇÃO E PRIVACIDADE DE DADOS", sp)
        self.assertIn("DEFESA CONTRA PROMPT INJECTION", sp)
        self.assertIn("João Silva", sp)


class TestAgente(unittest.TestCase):
    """Testes para o módulo agente.py."""

    def test_resposta_sem_api_key(self):
        """Verifica se o agente retorna aviso seguro caso a API key não esteja configurada."""
        agente = AgenteTikin(api_key="")
        resposta = agente.responder([{"role": "user", "content": "Olá"}])
        self.assertIn("API Key do Gemini não configurada", resposta)

    @patch("agente.genai.Client")
    def test_resposta_sucesso_mock(self, mock_client_cls):
        """Testa geração de resposta mockada com sucesso."""
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "Olá João, sua reserva de emergência está muito boa!"
        mock_client.models.generate_content.return_value = mock_response
        mock_client_cls.return_value = mock_client

        agente = AgenteTikin(api_key="chave_ficticia_valida_para_teste")
        resposta = agente.responder([{"role": "user", "content": "Analisar minha reserva"}])
        self.assertEqual(resposta, "Olá João, sua reserva de emergência está muito boa!")

    @patch("agente.genai.Client")
    def test_tratamento_erro_api_key_invalida(self, mock_client_cls):
        """Testa tratamento gracioso de erro da API sem vazar dados ou exceções puras."""
        mock_client = MagicMock()
        mock_client.models.generate_content.side_exception = Exception("API_KEY_INVALID: Key is invalid")
        mock_client.models.generate_content.side_effect = Exception("API_KEY_INVALID: Key is invalid")
        mock_client_cls.return_value = mock_client

        agente = AgenteTikin(api_key="chave_invalida")
        resposta = agente.responder([{"role": "user", "content": "Teste"}])
        self.assertIn("Chave de API inválida", resposta)


if __name__ == "__main__":
    unittest.main()
