"""
Módulo de integração com o modelo Gemini via SDK google-genai.

Gerencia a conexão com a API do Gemini, formata a chamada com o system prompt e histórico,
e garante tratamento seguro de erros.
"""

from google import genai
from google.genai import types

import config
from prompts import obter_system_prompt


class AgenteTikin:
    """Classe responsável pela integração do Tikin com o modelo Gemini."""

    def __init__(self, api_key: str | None = None):
        """Inicializa o agente com a chave de API fornecida ou das configurações."""
        self.api_key = api_key if api_key is not None else config.get_api_key()
        self.client = None

        if self._chave_valida(self.api_key):
            try:
                self.client = genai.Client(api_key=self.api_key)
            except Exception:
                self.client = None

    def _chave_valida(self, key: str | None) -> bool:
        """Verifica se a chave não é vazia nem o placeholder padrão."""
        if not key:
            return False
        return key.strip() not in ("", "sua_chave_aqui")

    def responder(self, historico_mensagens: list[dict]) -> str:
        """
        Recebe o histórico de conversas e gera a resposta do Tikin.

        Args:
            historico_mensagens: Lista de dicionários no formato [{"role": "user"|"assistant", "content": "..."}]

        Returns:
            String contendo a resposta gerada pelo modelo ou mensagem explicativa de erro.
        """
        if not self.client:
            return (
                "⚠️ **API Key do Gemini não configurada.**\n\n"
                "Para utilizar o assistente Tikin, configure sua `GEMINI_API_KEY` no arquivo `.env` "
                "ou informe a chave no painel lateral."
            )

        system_instruction = obter_system_prompt()

        # Converte histórico para o formato do SDK google-genai
        contents = []
        for msg in historico_mensagens:
            role = "user" if msg["role"] == "user" else "model"
            contents.append(
                types.Content(
                    role=role,
                    parts=[types.Part.from_text(text=msg["content"])],
                )
            )

        gen_config = types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=config.TEMPERATURE,
            max_output_tokens=config.MAX_OUTPUT_TOKENS,
        )

        try:
            response = self.client.models.generate_content(
                model=config.MODEL_NAME,
                contents=contents,
                config=gen_config,
            )
            if response and response.text:
                return response.text
            return "Não foi possível obter uma resposta do assistente no momento. Tente novamente."
        except Exception as err:
            err_msg = str(err).lower()
            if "api_key" in err_msg or "unauthorized" in err_msg or "400" in err_msg:
                return "⚠️ **Chave de API inválida ou sem permissão.** Por favor, verifique a `GEMINI_API_KEY` informada."
            elif "quota" in err_msg or "429" in err_msg:
                return "⚠️ **Limite de cota excedido.** Aguarde alguns instantes antes de enviar uma nova mensagem."
            else:
                return "⚠️ **Ocorreu um erro ao comunicar com o serviço de IA.** Por favor, tente novamente mais tarde."
