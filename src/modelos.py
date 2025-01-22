from pydantic import BaseModel
from typing import List, Dict

class Mensaje(BaseModel):
    role: str = "system"
    msg: str
    
class ContextoUsuario(BaseModel):
    nombre_usuario: str
    mensajes: List[Mensaje] = []

    def agregar_mensaje(self, msg: Mensaje) -> None:
        # Esto lo hago para que el contexto del usuario no sea infinito.
        if len(self.mensajes) >= 20:
            self.mensajes.pop(2)
        self.mensajes.append(msg)
        
class Contexto(BaseModel):
    contexto: Dict[str, ContextoUsuario] = {}
    