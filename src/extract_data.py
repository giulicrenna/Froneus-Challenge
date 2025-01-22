import re
from typing import List
from PyPDF2 import PdfReader

def extraer_texto_de_pdf(ruta_pdf: str) -> str:
    """
    Extrae el texto de un archivo PDF.
    Args:
        ruta_pdf (str): Ruta del archivo PDF.
    Returns:
        str: Texto extraído del PDF.
    """
    lector = PdfReader(ruta_pdf)
    
    texto = ""
    
    for pagina in lector.pages:
        texto += pagina.extract_text()
    
    return texto

def limpiar_caracteres_extraños(texto: str) -> str:
    """
    Limpia caracteres extraños del texto, dejando solo letras, números y espacios.
    Args:
        texto (str): Texto a limpiar.
    Returns:
        str: Texto limpio.
    """
    # Elimina caracteres no alfanuméricos
    return re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑüÜ\s]', '', texto)

def dividir_texto_en_fragmentos(texto: str, chunk_size: int = 500) -> List[str]:
    """
    Divide el texto en fragmentos de tamaño fijo sin cortar palabras, limpiando caracteres extraños.
    Args:
        texto (str): Texto completo.
        tamaño_fragmento (int): Tamaño de cada fragmento.
    Returns:
        list: Lista de fragmentos de texto.
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
