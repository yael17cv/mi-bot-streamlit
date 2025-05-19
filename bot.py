import streamlit as st

# Base de conocimiento con 10 preguntas y respuestas
knowledge_base = {
    "¿cuál es la capital de francia?": "La capital de Francia es París.",
    "¿quién escribió cien años de soledad?": "Gabriel García Márquez.",
    "¿cuál es el océano más grande del mundo?": "El océano Pacífico.",
    "¿qué planeta es conocido como el planeta rojo?": "Marte.",
    "¿quién pintó la última cena?": "Leonardo da Vinci.",
    "¿cuál es el país más grande del mundo?": "Rusia.",
    "¿en qué año llegó el hombre a la luna?": "En 1969.",
    "¿qué gas respiramos para vivir?": "Oxígeno.",
    "¿cuántos continentes hay?": "Hay siete continentes.",
    "¿qué instrumento mide los sismos?": "El sismógrafo."
}

# Función para buscar la respuesta
def get_response(user_input):
    user_input = user_input.lower().strip()
    for question, answer in knowledge_base.items():
        if user_input == question:
            return answer
    return "Lo siento, no tengo una respuesta para eso."

# INTERFAZ DE USUARIO
st.title("Bot de Preguntas y Respuestas")

user_input = st.text_input("Escribe una pregunta")

if user_input:
    response = get_response(user_input)
    st.write(response)
