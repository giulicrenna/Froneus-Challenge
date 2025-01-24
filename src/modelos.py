from pydantic import BaseModel
from typing import List, Dict


class Mensaje(BaseModel):
    """
    Representa un mensaje en el contexto de un usuario.

    Atributos:
        role (str): Rol asociado al mensaje (por ejemplo, "system", "user", "assistant"). Por defecto es "system".
        msg (str): Contenido del mensaje.
    """

    role: str = "system"
    msg: str


class ContextoUsuario(BaseModel):
    """
    Representa el contexto de un usuario, incluyendo su nombre y una lista de mensajes.

    Atributos:
        nombre_usuario (str): Nombre del usuario.
        mensajes (List[Mensaje]): Lista de mensajes asociados al usuario. Por defecto es una lista vacía.
    """

    nombre_usuario: str
    mensajes: List[Mensaje] = []

    def agregar_mensaje(self, msg: Mensaje) -> None:
        """
        Agrega un mensaje al contexto del usuario. Si la lista de mensajes supera los 20 elementos,
        se elimina el tercer mensaje (índice 2) para mantener un límite.

        Parámetros:
            msg (Mensaje): Mensaje que se desea agregar al contexto del usuario.

        Retorna:
            None
        """
        # Esto lo hago para que el contexto del usuario no sea infinito.
        if len(self.mensajes) >= 20:
            self.mensajes.pop(2)  # Elimina el tercer mensaje
        self.mensajes.append(msg)


class Contexto(BaseModel):
    """
    Representa un contexto global que almacena los contextos de múltiples usuarios.

    Atributos:
        contexto (Dict[str, ContextoUsuario]): Diccionario que mapea nombres de usuarios a sus respectivos contextos.
                                              Por defecto es un diccionario vacío.
    """

    contexto: Dict[str, ContextoUsuario] = {}
