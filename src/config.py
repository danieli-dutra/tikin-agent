"""
Configurações do Tikin — Assistente Financeiro Inteligente.

Carrega variáveis de ambiente e define parâmetros do modelo.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega .env do diretório raiz do projeto
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJECT_ROOT / ".env")

# Modelo e parâmetros
MODEL_NAME = "gemini-3.6-flash"
TEMPERATURE = 0.7
MAX_OUTPUT_TOKENS = 2048

# Caminhos dos dados
DATA_DIR = _PROJECT_ROOT / "data"

# Validação da API key
def get_api_key() -> str | None:
    """Retorna a API key ou None se não configurada."""
    return os.environ.get("GEMINI_API_KEY")


def is_api_key_configured() -> bool:
    """Verifica se a API key está presente e não é o placeholder."""
    key = get_api_key()
    if not key:
        return False
    if key.strip() in ("", "sua_chave_aqui"):
        return False
    return True
