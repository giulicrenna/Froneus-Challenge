import chromadb
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Dict

cliente = chromadb.PersistentClient(
    path=os.path.join(os.getcwd(), "data", "embeddings")
)

coleccion = cliente.get_or_create_collection(name="juegos_de_tronos")


def generar_embeddings(
    fragmentos_texto: List[str], nombre_modelo: str = "all-MiniLM-L6-v2"
) -> List[np.ndarray]:
    """
    Genera embeddings (vectores numéricos) para una lista de fragmentos de texto utilizando un modelo de lenguaje.

    Parámetros:
        fragmentos_texto (List[str]): Lista de cadenas de texto para las cuales se generarán los embeddings.
        nombre_modelo (str, opcional): Nombre del modelo de Sentence Transformers a utilizar. Por defecto es "all-MiniLM-L6-v2".

    Retorna:
        List[np.ndarray]: Lista de embeddings (vectores) generados para cada fragmento de texto.
    """
    modelo = SentenceTransformer(nombre_modelo)
    
    return modelo.encode(fragmentos_texto).tolist()


def guardar_embeddings_en_chroma(
    embeddings: List[np.ndarray], textos: List[str], nombre_coleccion: str
) -> None:
    """
    Guarda los embeddings y los textos asociados en una colección de ChromaDB.

    Parámetros:
        embeddings (List[np.ndarray]): Lista de embeddings (vectores) a almacenar.
        textos (List[str]): Lista de textos asociados a los embeddings.
        nombre_coleccion (str): Nombre de la colección en ChromaDB donde se guardarán los datos.
    """
    ids = [f"doc_{i}" for i in range(len(embeddings))]
    
    coleccion.add(embeddings=embeddings, documents=textos, ids=ids)


def consulta_semantica(
    texto_consulta: str, top_k: int = 5, nombre_modelo: str = "all-MiniLM-L6-v2"
) -> List[Dict]:
    """
    Realiza una consulta semántica en la colección de ChromaDB para encontrar los textos más similares al texto de consulta.

    Parámetros:
        texto_consulta (str): Texto de consulta para el cual se buscarán resultados similares.
        top_k (int, opcional): Número de resultados más similares a devolver. Por defecto es 5.
        nombre_modelo (str, opcional): Nombre del modelo de Sentence Transformers a utilizar. Por defecto es "all-MiniLM-L6-v2".

    Retorna:
        List[Dict]: Lista de diccionarios con los resultados más similares.
    """
    modelo = SentenceTransformer(nombre_modelo)

    embedding_consulta = modelo.encode([texto_consulta]).tolist()

    resultados = coleccion.query(query_embeddings=embedding_consulta, n_results=top_k)

    return resultados


def similitud_coseno(
    texto1: str, texto2: str, nombre_modelo: str = "all-MiniLM-L6-v2"
) -> float:
    """
    Calcula la similitud coseno entre dos textos utilizando sus embeddings.

    Parámetros:
        texto1 (str): Primer texto para comparar.
        texto2 (str): Segundo texto para comparar.
        nombre_modelo (str, opcional): Nombre del modelo de Sentence Transformers a utilizar. Por defecto es "all-MiniLM-L6-v2".

    Retorna:
        float: Valor de similitud coseno entre los dos textos (rango de -1 a 1).
    """
    modelo = SentenceTransformer(nombre_modelo)

    embeddings = modelo.encode([texto1, texto2])

    similitud = np.dot(embeddings[0], embeddings[1]) / (
        np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1])
    )

    return similitud


def eliminar_documento_por_id(id_documento: str) -> None:
    """
    Elimina un documento de la colección de ChromaDB utilizando su ID.

    Parámetros:
        id_documento (str): ID del documento a eliminar.
    """
    coleccion.delete(ids=[id_documento])
    
    print(f"Documento con ID '{id_documento}' eliminado.")


def limpiar_chromadb(collection_name: str = None) -> None:
    """
    Elimina una colección completa de ChromaDB.

    Parámetros:
        collection_name (str, opcional): Nombre de la colección a eliminar. Si no se proporciona, no se realiza ninguna acción.
    """
    try:
        cliente.delete_collection(collection_name)
        
        print(f"Colección '{collection_name}' borrada.")
    except Exception as e:
        print(f"Error eliminando '{collection_name}': {e}")
