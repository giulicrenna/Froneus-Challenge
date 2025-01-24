from src.chroma import *
from src.extract_data import *
from src.cprint import cprint
from src.modelos import ContextoUsuario
from src.gpt import contexto_global, mensajes_presentacion, agregar_mensaje_contexto, obtener_mensajes_contexto, llamar_api_openai
from dotenv import load_dotenv
from typing import List
from numpy import ndarray as Array
from random import choice
import streamlit as st
import os

st.set_page_config(page_title="Froneus Challenge", page_icon=":snowflake:")

load_dotenv()

def inicializar_db(pdf_path: str) -> None:
    """
    Orquesta el proceso completo desde la extracción del texto del PDF hasta el almacenamiento en ChromaDB.
    Parámetros:
        pdf_path (str): Ruta del archivo PDF.
    """
    text: str = extraer_texto_de_pdf(pdf_path)
    cprint("Texto extraído del PDF.", "INFO")
    
    text_chunks: List[str] = dividir_texto_en_fragmentos(text, chunk_size=500)
    cprint("Texto dividido en fragmentos.", "INFO")

    cprint("Generando embeddings...", "INFO")
    embeddings: List[Array] = generar_embeddings(text_chunks)

    cprint("Guardando embeddings en ChromaDB...", "INFO")
    guardar_embeddings_en_chroma(embeddings, text_chunks, "juegos_de_tronos")


if not os.path.exists(os.path.join(os.getcwd(), "data", "embeddings")):
    cprint("Creando Base de datos vectorial...", "INFO")
    pdf_path: str = os.path.join(os.getcwd(),
                                    "data",
                                    "pdf",
                                    "Juego de tronos - Cancion de hielo y fuego.pdf")
    inicializar_db(pdf_path)
    cprint("Base de datos vectorial creada.", "COMPLETE")
else:
    cprint("Base de datos vectorial ya existe.", "WARNING")
    
"""
A partir de acá genero el Streamlit para la posterior visualización.
"""
st.title(":snowflake: Chatbot de Juego de Tronos")



with st.sidebar:
    st.image(os.path.join(os.getcwd(), 'static', 'froneus.png'), use_container_width=True)
    usuario = st.text_input("Usuario")

    if usuario == "":
        st.warning("Debe proporcionar un nombre de usuario.")

    if st.button("Cargar usuario"):
        if usuario:
            if usuario not in contexto_global.contexto:
                contexto_global.contexto[usuario] = ContextoUsuario(nombre_usuario=usuario)
            st.toast("Usuario cargado!")
        else:
            st.warning("Por favor, ingresa un nombre de usuario.")
            
    st.info("""
            Este chatbot forma parte del challenge de Froneus. \n\n
            Su objetivo es responder preguntas sobre el primer libro de Game of Thrones. \n\n
            Para comenzar a usarlo debe ingresar un nombre de usuario y escribir una pregunta en el chat.
            """)

if usuario and usuario in contexto_global.contexto:
    with st.chat_message("assistant"):
        st.markdown(choice(mensajes_presentacion))
        
    mensajes = obtener_mensajes_contexto(usuario)
    
    for mensaje in mensajes:
        with st.chat_message(mensaje["role"]):
            st.markdown(mensaje["content"])

if prompt := st.chat_input("Escribe tu pregunta:", disabled=True if usuario == "" else False):
    cprint(f"Usuario '{usuario}' preguntó: {prompt}", "INFO")
    
    with st.chat_message("user"):
        st.markdown(prompt)

    cprint("Realizando consulta semántica", "INIT")
    consulta = consulta_semantica(texto_consulta=prompt, top_k=5)
    
    documentos: List[str] = consulta["documents"]
    
    cprint("Llamando a la API de OpenAI...", "INFO")
    respuesta: str = llamar_api_openai(usuario=usuario, pregunta=prompt, documentos=documentos)

    with st.chat_message("assistant"):
        cprint(f"Respuesta del chatbot generada satisfactoriamente.", "COMPLETE")
        st.markdown(respuesta)
