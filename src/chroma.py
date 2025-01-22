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
    modelo = SentenceTransformer(nombre_modelo)

    return modelo.encode(fragmentos_texto).tolist()


def guardar_embeddings_en_chroma(
    embeddings: List[np.ndarray], textos: List[str], nombre_coleccion: str
) -> None:
    ids = [f"doc_{i}" for i in range(len(embeddings))]

    coleccion.add(embeddings=embeddings, documents=textos, ids=ids)


def consulta_semantica(
    texto_consulta: str, top_k: int = 5, nombre_modelo: str = "all-MiniLM-L6-v2"
) -> List[Dict]:
    modelo = SentenceTransformer(nombre_modelo)

    embedding_consulta = modelo.encode([texto_consulta]).tolist()

    resultados = coleccion.query(query_embeddings=embedding_consulta, n_results=top_k)

    return resultados


def similitud_coseno(
    texto1: str, texto2: str, nombre_modelo: str = "all-MiniLM-L6-v2"
) -> float:
    modelo = SentenceTransformer(nombre_modelo)

    embeddings = modelo.encode([texto1, texto2])

    similitud = np.dot(embeddings[0], embeddings[1]) / (
        np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1])
    )

    return similitud


def eliminar_documento_por_id(id_documento: str):
    coleccion.delete(ids=[id_documento])

    print(f"Documento con ID '{id_documento}' eliminado.")

def limpiar_chromadb(collection_name: str = None):
  try:
      cliente.delete_collection(collection_name)
      
      print(f"Colleccion '{collection_name}' borrada.")
      
  except Exception as e:
      print(f"Error eliminando '{collection_name}': {e}")
