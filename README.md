# Chatbot de Froneus

El **Chatbot de Froneus** es un asistente virtual diseñado para responder preguntas relacionadas exclusivamente con el libro *"Juego de Tronos"* de la serie *"Canción de Hielo y Fuego"* de George R. R. Martin.

Este proyecto utiliza *Streamlit* para la interfaz web y una arquitectura basada en modelos de lenguaje para proporcionar respuestas precisas y contextuales.

---

## Características
- Responde exclusivamente preguntas sobre el libro *Juego de Tronos*.
- Fácil instalación y despliegue.
- Disponible para ejecución local con entornos virtuales (*venv*) y mediante contenedores con *Docker Compose*.

---

## Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente:

- **Python** (versión 3.8 o superior).
- **Docker** y **Docker Compose** instalados para la opción de despliegue con contenedores.
- Acceso a internet para instalar las dependencias del proyecto.

---

## Instalación

### Instalación con venv en Windows

1. Clona el repositorio del proyecto:
   ```cmd
   git clone https://github.com/usuario/chatbot-froneus.git
   cd chatbot-froneus
   ```

2. Crea un entorno virtual:
   ```cmd
   python -m venv venv
   ```

3. Activa el entorno virtual:
   ```cmd
   .\venv\Scripts\activate
   ```

4. Instala las dependencias:
   ```cmd
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Ejecuta la aplicación:
   ```cmd
   streamlit run main.py
   ```

6. Abre tu navegador en [http://localhost:8501](http://localhost:8501).

---

### Instalación con venv en Linux

1. Clona el repositorio del proyecto:
   ```bash
   git clone https://github.com/usuario/chatbot-froneus.git
   cd chatbot-froneus
   ```

2. Crea un entorno virtual:
   ```bash
   python3 -m venv venv
   ```

3. Activa el entorno virtual:
   ```bash
   source venv/bin/activate
   ```

4. Instala las dependencias:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. Ejecuta la aplicación:
   ```bash
   streamlit run main.py
   ```

6. Abre tu navegador en [http://localhost:8501](http://localhost:8501).

---

### Instalación con Docker Compose

1. Clona el repositorio del proyecto:
   ```bash
   git clone https://github.com/usuario/chatbot-froneus.git
   cd chatbot-froneus
   ```

2. Construye y ejecuta el contenedor:
   ```bash
   docker-compose up --build
   ```

3. Abre tu navegador en [http://localhost:8082](http://localhost:8082).

4. Para detener el contenedor, utiliza:
   ```bash
   docker-compose down
   ```

---

## Notas Adicionales
- Asegúrate de que el puerto especificado (8082 para Docker o 8501 para ejecución local) no esté ocupado por otra aplicación.
- En caso de problemas con las dependencias, verifica la compatibilidad de las versiones en el archivo `requirements.txt`.


