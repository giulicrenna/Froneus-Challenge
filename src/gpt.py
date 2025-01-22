from openai import OpenAI
from openai import ChatCompletion
from dotenv import load_dotenv
from typing import List
from src.modelos import *
from random import choice
import streamlit as st
import os

load_dotenv()

st.session_state.contexto_global = Contexto()

contexto_global = st.session_state.contexto_global

CONTEXT: str = """
Eres un chatbot experto en responder exclusivamente preguntas sobre el libro "Juego de Tronos" de George R. R. Martin.  
Tu objetivo es proporcionar respuestas precisas y detalladas basadas únicamente en el contenido de este libro.  
No debes responder preguntas relacionadas con la serie de televisión, otros libros de la saga, ni temas ajenos al libro.  
Por favor, limita tus respuestas estrictamente a la información contenida en "Juego de Tronos".  
"""

mensajes_presentacion: List[str] = [
    "¡Hola! Soy Froneus, tu asistente especializado en responder preguntas sobre el libro *Juego de Tronos*.",
    "¡Bienvenido! Soy el chatbot de Froneus, aquí para ayudarte con cualquier duda sobre *Juego de Tronos*.",
    "¡Hola! Estoy aquí para resolver todas tus preguntas sobre el libro *Juego de Tronos* de George R. R. Martin.",
    "¡Saludos! Soy el chatbot de Froneus, experto en el universo de *Juego de Tronos*. ¿En qué puedo ayudarte?",
    "Hola, soy Froneus. Mi misión es responder exclusivamente preguntas relacionadas con el libro *Juego de Tronos*.",
    "¡Hola! Soy tu asistente literario especializado en *Juego de Tronos*. ¿Qué te gustaría saber?",
    "¡Bienvenido al mundo de *Juego de Tronos*! Soy el chatbot de Froneus, listo para responder tus preguntas.",
    "¡Hola! Soy el experto en *Juego de Tronos* que estabas buscando. ¿Qué necesitas saber?",
    "¡Hola! Aquí Froneus, tu guía exclusivo para todo lo relacionado con el libro *Juego de Tronos*.",
    "¡Saludos! Soy el chatbot de Froneus. ¿Tienes preguntas sobre *Juego de Tronos*? Estoy listo para responder."
]


def agregar_mensaje_contexto(usuario: str, role: str, mensaje: str) -> None:
    if usuario not in contexto_global.contexto:
        contexto_global.contexto[usuario] = ContextoUsuario(nombre_usuario=usuario)

    msg = Mensaje(role=role, msg=mensaje)

    contexto_global.contexto[usuario].agregar_mensaje(msg)

def obtener_mensajes_contexto(usuario: str) -> List[Dict[str, str]]:    
    mensajes = [{"role": msg.role, "content": msg.msg} for msg in contexto_global.contexto[usuario].mensajes]
    
    return mensajes


def llamar_api_openai(usuario: str, pregunta: str, documentos: List[str]) -> str:
    agregar_mensaje_contexto(usuario, "user", pregunta)

    # Hago una copia ya que no me intera guardar los documentos de la query en el contexto.
    mensajes = obtener_mensajes_contexto(usuario).copy()
    
    """
    Preparo el contexto del chatbot
    """
    mensajes.insert(0, {"role": "system", "content" : CONTEXT})
    mensajes[0]["content"] += "\nResponder en base a la siguiente información:\n"
    
    for documento in documentos:
        mensajes[0]["content"] += f"\n{documento}"
    
    client = OpenAI(api_key=os.getenv("KEY"))
    
    response = client.chat.completions.create(model="gpt-3.5-turbo",
                                                messages=mensajes)
    
    respuesta_texto = response.choices[0].message.content
    
    agregar_mensaje_contexto(usuario, "assistant", respuesta_texto)

    return respuesta_texto

