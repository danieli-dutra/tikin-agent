"""
Aplicação Streamlit — Tikin: Assistente Financeiro Inteligente.

Interface interativa web com chat, informações do cliente, atalhos de perguntas
e orientações de segurança digital.
"""

import sys
from pathlib import Path
import streamlit as st

# Garante inclusão da pasta src no PYTHONPATH
_SRC_DIR = Path(__file__).resolve().parent / "src"
if str(_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(_SRC_DIR))

import config
import dados
from agente import AgenteTikin

# Configuração da página Streamlit
st.set_page_config(
    page_title="Tikin - Assistente Financeiro",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilização CSS customizada
st.markdown(
    """
    <style>
    /* Estilo do título principal */
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E88E5;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #555555;
        margin-bottom: 1.5rem;
    }
    /* Estilo dos cards de perfil */
    .profile-card {
        background-color: #F8F9FA;
        border-left: 4px solid #1E88E5;
        padding: 1rem;
        border-radius: 6px;
        margin-bottom: 1rem;
    }
    /* Botões rápidos */
    .stButton>button {
        border-radius: 8px;
        font-weight: 500;
    }
    /* Desativa ícones de âncora nos títulos */
    .header-anchor {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def inicializar_estado():
    """Inicializa variáveis na sessão do Streamlit."""
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Olá, João! Sou o **Tikin**, seu assistente financeiro inteligente. 🤖💰\n\n"
                    "Estou aqui para ajudar com suas finanças, opções de investimento, análise de "
                    "gastos e tirar dúvidas de segurança digital.\n\n"
                    "Como posso te ajudar hoje?"
                ),
            }
        ]


def main():
    inicializar_estado()

    # --- BARRA LATERAL (SIDEBAR) ---
    with st.sidebar:
        st.markdown("## 💰 Tikin Finance")
        st.caption("Assistente Pessoal & Segurança Digital")
        st.divider()

        # Configuração de API Key
        st.subheader("🔑 Configuração da API Key")
        api_key_env = config.get_api_key()
        api_key_configured = config.is_api_key_configured()

        if api_key_configured:
            st.success("API Key configurada via `.env`", icon="✅")
            user_api_key = api_key_env
        else:
            st.warning("API Key não detectada no `.env`", icon="⚠️")
            user_api_key = st.text_input(
                "Informe sua GEMINI_API_KEY:",
                type="password",
                help="Obtenha uma chave em https://aistudio.google.com/",
            )

        st.divider()

        # Painel do Perfil do Cliente
        st.subheader("👤 Perfil do Cliente")
        st.markdown(
            """
            **Cliente:** João Silva  
            **Profissão:** Analista de Sistemas  
            **Renda Mensal:** R$ 5.000,00  
            **Perfil:** Moderado  
            **Objetivo:** Reserva de emergência  
            **Patrimônio:** R$ 15.000,00  
            **Reserva Atual:** R$ 10.000,00  
            """
        )

        st.divider()

        # Dicas rápidas de segurança
        with st.expander("🛡️ Dicas de Segurança Digital"):
            st.markdown(
                """
                - **Nunca** compartilhe senhas ou CVV.
                - Bancos **não ligam** pedindo códigos por SMS.
                - Verifique os dados do destinatário antes de fazer um Pix.
                - Mantenha seu app bancário atualizado.
                """
            )

        # Botão para reiniciar chat
        if st.button("🗑️ Limpar Conversa", use_container_width=True):
            st.session_state.messages = [
                {
                    "role": "assistant",
                    "content": "Conversa reiniciada! Como posso ajudar você agora, João?",
                }
            ]
            st.rerun()

    # --- ÁREA PRINCIPAL ---
    st.markdown('<div class="main-title">💰 Tikin — Assistente Financeiro</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-title">Seu copiloto inteligente para investimentos, planejamento financeiro e proteção digital.</div>',
        unsafe_allow_html=True,
    )

    # Botões de perguntas rápidas (Sugestões)
    st.markdown("##### 💡 Sugestões de perguntas rápidas:")
    col1, col2, col3, col4 = st.columns(4)

    sugestao_selecionada = None
    with col1:
        if st.button("📊 Analisar gastos", use_container_width=True):
            sugestao_selecionada = "Pode fazer uma análise rápida das minhas despesas de outubro?"
    with col2:
        if st.button("📈 Onde investir?", use_container_width=True):
            sugestao_selecionada = "Qual o melhor produto financeiro disponível para meu perfil moderado?"
    with col3:
        if st.button("🛡️ Evitar Golpe Pix", use_container_width=True):
            sugestao_selecionada = "Como posso me proteger do Golpe do Pix?"
    with col4:
        if st.button("🎯 Reserva Emergência", use_container_width=True):
            sugestao_selecionada = "Minha reserva de emergência atual de R$ 10.000 é suficiente para a minha renda?"

    # Exibe o histórico de mensagens
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"], anchors=False)

    # Entrada do usuário (via chat_input ou botão rápido)
    prompt_usuario = st.chat_input("Digite sua dúvida financeira ou sobre segurança...")

    prompt_final = sugestao_selecionada or prompt_usuario

    if prompt_final:
        # Registra a mensagem do usuário na tela e no histórico
        st.session_state.messages.append({"role": "user", "content": prompt_final})
        with st.chat_message("user"):
            st.markdown(prompt_final, anchors=False)

        # Instancia agente e gera resposta
        agente = AgenteTikin(api_key=user_api_key)

        with st.chat_message("assistant"):
            with st.spinner("Tikin está consultando sua base financeira..."):
                resposta = agente.responder(st.session_state.messages)
                st.markdown(resposta, anchors=False)

        # Adiciona resposta do assistente ao histórico
        st.session_state.messages.append({"role": "assistant", "content": resposta})


if __name__ == "__main__":
    main()
