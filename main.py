import streamlit as st
import requests

st.title("🤖 Chatbot de Geometría")

API_KEY = "TU_API_KEY"

pregunta = st.text_input("Escribe tu pregunta:")

if st.button("Enviar"):
    if pregunta:
        respuesta = requests.post(
            "https://api.deepseek.com/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}"
            },
            json={
                "model": "deepseek-chat",
                "messages": [
                    {
                        "role": "system",
                        "content": "Eres un asistente de matemáticas. Ayuda a estudiantes de décimo con áreas, perímetros y figuras geométricas. Explica de manera sencilla."
                    },
                    {
                        "role": "user",
                        "content": pregunta
                    }
                ]
            }
        )

        if respuesta.status_code == 200:
            datos = respuesta.json()
            mensaje = datos["choices"][0]["message"]["content"]
            st.write("🤖", mensaje)
        else:
            st.error("Error al conectar con el chatbot.")
    else:
        st.warning("Escribe una pregunta.")
