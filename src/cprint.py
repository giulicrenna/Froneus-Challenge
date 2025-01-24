from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

PROCESS_COLORS = {
    "INIT": Fore.BLUE,
    "COMPLETE": Fore.GREEN,
    "ERROR": Fore.RED,
    "WARNING": Fore.YELLOW,
    "INFO": Fore.CYAN,
}

def cprint(msg: str, proceso: str) -> None:
    """
    Imprime un mensaje en la consola con un formato específico, incluyendo un color asociado al tipo de proceso.

    Parámetros:
        msg (str): El mensaje que se desea imprimir.
        proceso (str): El tipo de proceso asociado al mensaje (por ejemplo, "INIT", "COMPLETE", "ERROR", etc.).
                      Este valor determina el color del mensaje.

    Retorna:
        None
    """
    current_time = datetime.now().strftime("%H:%M:%S")
    
    color = PROCESS_COLORS.get(proceso.upper(), Fore.WHITE)
    
    print(f"{color}[{proceso}]{Style.RESET_ALL} {current_time}: {msg}")


if __name__ == "__main__":
    cprint("El proceso ha iniciado.", "INIT")
    cprint("Se completó la operación.", "COMPLETE")
    cprint("Hubo un error inesperado.", "ERROR")
    cprint("El espacio en disco está bajo.", "WARNING")
    cprint("Conexión establecida.", "INFO")
    cprint("Proceso desconocido.", "OTHER")