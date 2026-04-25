# 🤖 Chatbot com IA usando Gemini e Streamlit

🔗 **Acesse o chatbot:** https://meu-chatbot-gemini.streamlit.app/

Este é um projeto de chatbot interativo desenvolvido inteiramente em **Python**, que une a simplicidade do **Streamlit** para o frontend à inteligência do modelo **Google Gemini (GenAI)** no backend. 

A aplicação oferece uma interface de chat fluida, com suporte a **histórico de conversa persistente** (memória de contexto), permitindo que a IA mantenha o contexto do diálogo durante toda a sessão.

## Funcionalidades

- Interface de chat interativa com Streamlit
- Uso do modelo **Gemini Flash**
- Histórico de conversa mantido durante a sessão
- Botão para limpar a conversa
- Tratamento de erro para limite de cota da API
- Uso de variável de ambiente para proteger a chave da API

## Tecnologias utilizadas

- Python 3.14.2
- Streamlit
- Google Gemini (google-genai)

## ⚠️ Observações

- O chatbot pode levar alguns segundos para responder devido à latência da API  
- É necessário estar conectado à internet para utilizar a aplicação  
- O desempenho pode variar de acordo com a disponibilidade da API  