# Streamlit -> possibilita, apenas com Python, criar o frontend e o backend
# IA: genai

# Para rodar, digite no terminal:
# streamlit run genai_api.py

import streamlit as st
from google import genai
import time
from google.genai.errors import ClientError
import os

# Título na aba do navegador
st.set_page_config(page_title="Chatbot com IA", page_icon="🤖")

# Título
st.write("# Chatbot com IA")  # Markdown

# Chave API (usando variável de ambiente)
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Chave API não encontrada. Configure a variável de ambiente GOOGLE_API_KEY.")
    st.stop()

# Conexão com GenAI
modelo_ia = genai.Client(api_key=api_key)

# Definição do prompt
prompt = "Responde de maneira educada e simpática"

# Verificar se já existe uma lista de mensagens
if not "lista_mensagens" in st.session_state:  # session_state = memória da sessão do navegador/cookies
    st.session_state["lista_mensagens"] = []

# Input do chat (campo de mensagem)
texto_usuario = st.chat_input("Digite sua mensagem")

# Mostrar todas as mensagens na tela
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

# A cada mensagem que o usário enviar:   
if texto_usuario:

    historico_api = [{"role": "user", "parts": [{"text": prompt}]}]

    # Adicionar mensagens anteriores no histórico
    for msg in st.session_state["lista_mensagens"]:
    # Traduzir 'assistant' do Streamlit para 'model' da API
        if msg["role"] == "assistant":
            role_api = "model"
        else:
            role_api = "user"

        historico_api.append({"role": role_api, "parts": [{"text": msg["content"]}]})

    # Criar o chat
    chat = modelo_ia.chats.create(model="gemini-flash-latest", history=historico_api)

    # Mostrar a mensagem que o usuário enviou no chat
    st.chat_message("user").write(texto_usuario) 
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    # Pegar o texto do usuário e enviar para uma IA responder
    try:
        resposta_ia = chat.send_message(texto_usuario)
    except ClientError as e:
        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
            st.warning("A IA está descansando um pouco (limite de cota). Tente novamente em alguns segundos.")
            time.sleep(35)
        else:
            st.error(f"Ocorreu um erro: {e}")
            st.stop()

    print(resposta_ia)  # A IA retorna várias informações. Precisa selecionar só o que se quer.

    # Exibir a resposta da IA na tela
    texto_resposta_ia = resposta_ia.text # Selecionar só o texto de resposta
    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)


# Visualização no terminal
print(st.session_state["lista_mensagens"]) 
