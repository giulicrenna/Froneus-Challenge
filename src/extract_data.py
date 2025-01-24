import re
from typing import List
from PyPDF2 import PdfReader

def extraer_texto_de_pdf(ruta_pdf: str) -> str:
    """
    Extrae el texto de un archivo PDF.

    Parámetros:
        ruta_pdf (str): Ruta del archivo PDF del cual se extraerá el texto.

    Retorna:
        str: Texto extraído del PDF.
    """
    lector = PdfReader(ruta_pdf)
    texto = ""
    
    for pagina in lector.pages:
        texto += pagina.extract_text()
    
    return texto


def limpiar_caracteres_extraños(texto: str) -> str:
    """
    Limpia caracteres extraños del texto, dejando solo letras, números, espacios y caracteres especiales del español.

    Parámetros:
        texto (str): Texto que se desea limpiar.

    Retorna:
        str: Texto limpio, sin caracteres no deseados.
    """
    return re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\s]', '', texto)


def dividir_texto_en_fragmentos(texto: str, chunk_size: int = 500) -> List[str]:
    """
    Divide el texto en fragmentos de tamaño fijo sin cortar palabras, asegurándose de que cada fragmento no exceda el tamaño especificado.

    Parámetros:
        texto (str): Texto completo que se desea dividir.
        chunk_size (int, opcional): Tamaño máximo de cada fragmento. Por defecto es 500.

    Retorna:
        List[str]: Lista de fragmentos de texto.
    """
    texto_limpio = limpiar_caracteres_extraños(texto)
    palabras = texto_limpio.split()
    fragmentos = []
    fragmento_actual = []

    for palabra in palabras:
        if sum(len(p) for p in fragmento_actual) + len(fragmento_actual) + len(palabra) <= chunk_size:
            fragmento_actual.append(palabra)
        else:
            fragmentos.append(" ".join(fragmento_actual))
            fragmento_actual = [palabra]

    if fragmento_actual:
        fragmentos.append(" ".join(fragmento_actual))

    return fragmentos