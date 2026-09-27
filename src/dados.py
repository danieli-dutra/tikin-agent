"""
Carregamento e formatação dos dados da base de conhecimento do Tikin.

Lê os 5 arquivos de dados e os formata como texto legível
para injeção no system prompt.
"""

import json
import pandas as pd
from pathlib import Path

from config import DATA_DIR


def _ler_json(caminho: Path) -> dict | list:
    """Lê um arquivo JSON e retorna o conteúdo."""
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def _ler_csv(caminho: Path) -> pd.DataFrame:
    """Lê um arquivo CSV e retorna um DataFrame."""
    return pd.read_csv(caminho, encoding="utf-8")


def carregar_perfil() -> str:
    """Carrega e formata o perfil do investidor."""
    perfil = _ler_json(DATA_DIR / "perfil_investidor.json")
    linhas = []
    for chave, valor in perfil.items():
        nome = chave.replace("_", " ").capitalize()
        linhas.append(f"- {nome}: {valor}")
    return "\n".join(linhas)


def carregar_transacoes() -> str:
    """Carrega e formata as transações financeiras."""
    df = _ler_csv(DATA_DIR / "transacoes.csv")
    linhas = []
    for _, row in df.iterrows():
        tipo_label = "+" if row["tipo"] == "entrada" else "-"
        linhas.append(
            f"- {row['data']} | {row['descricao']} ({row['categoria']}) | "
            f"{tipo_label} R$ {row['valor']:.2f}"
        )
    return "\n".join(linhas)


def carregar_produtos() -> str:
    """Carrega e formata os produtos financeiros."""
    produtos = _ler_json(DATA_DIR / "produtos_financeiros.json")
    linhas = []
    for p in produtos:
        linhas.append(
            f"- {p['nome']}: {p['categoria']} | Risco: {p['risco']} | "
            f"Rentabilidade: {p['rentabilidade']} | "
            f"Aporte mínimo: R$ {p['aporte_minimo']:.2f} | "
            f"Liquidez: {p['liquidez']} | "
            f"Indicado para: {p['indicado_para']}"
        )
    return "\n".join(linhas)


def carregar_atendimentos() -> str:
    """Carrega e formata o histórico de atendimentos."""
    df = _ler_csv(DATA_DIR / "historico_atendimento.csv")
    linhas = []
    for _, row in df.iterrows():
        linhas.append(
            f"- {row['data']} | {row['canal']} | {row['tema']}: "
            f"{row['resumo']} (Resolvido: {row['resolvido']})"
        )
    return "\n".join(linhas)


def carregar_seguranca_digital() -> str:
    """Carrega e formata a base de segurança digital."""
    dados = _ler_json(DATA_DIR / "seguranca_digital.json")
    linhas = []

    linhas.append("GOLPES COMUNS:")
    for golpe in dados["golpes_comuns"]:
        linhas.append(f"- {golpe['nome']}: {golpe['descricao']}")
        linhas.append(f"  Como se proteger: {golpe['como_se_proteger']}")

    linhas.append("\nBOAS PRÁTICAS DE SEGURANÇA:")
    for pratica in dados["boas_praticas"]:
        linhas.append(f"- {pratica}")

    linhas.append("\nDADOS QUE NUNCA DEVEM SER COMPARTILHADOS:")
    for item in dados["o_que_nunca_compartilhar"]:
        linhas.append(f"- {item}")

    return "\n".join(linhas)


def carregar_todo_contexto() -> str:
    """Carrega todos os dados e retorna o contexto completo formatado."""
    secoes = [
        ("PERFIL DO CLIENTE", carregar_perfil()),
        ("TRANSAÇÕES RECENTES", carregar_transacoes()),
        ("PRODUTOS FINANCEIROS DISPONÍVEIS", carregar_produtos()),
        ("HISTÓRICO DE ATENDIMENTOS", carregar_atendimentos()),
        ("SEGURANÇA FINANCEIRA DIGITAL", carregar_seguranca_digital()),
    ]

    partes = []
    for titulo, conteudo in secoes:
        partes.append(f"=== {titulo} ===\n{conteudo}")

    return "\n\n".join(partes)
