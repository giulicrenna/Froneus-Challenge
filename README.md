# Chatbot de Froneus

El **Chatbot de Froneus** es un asistente virtual diseñado para responder preguntas relacionadas exclusivamente con el libro *"Juego de Tronos"* de la serie *"Canción de Hielo y Fuego"* de George R. R. Martin.

Este proyecto utiliza *Streamlit* para la interfaz web y una arquitectura basada en modelos de lenguaje para proporcionar respuestas precisas y contextuales.

---

## Preguntas

### ¿Qué lograste con tu modelo?
Con mi modelo, logré responder de manera satisfactoria las preguntas relacionadas con el libro Game of Thrones: Canción de Hielo y Fuego. Esto fue posible recuperando la información directamente de los documentos almacenados en la base de datos vectorial, lo que facilitó al modelo LLM comprender mejor el contexto.

### ¿Qué dificultades se te presentaron?,
Personalmente, lo que más me costó fue la parte del frontend. Aunque tengo bastante experiencia utilizando Streamlit, me considero más del backend.

### ¿Qué sugerís para el futuro?.

Hay varias cosas que se podrían mejorar en el futuro, como:  
1. Probar con un modelo de embeddings más potente y complejo.  
2. Hacer un preprocesamiento más detallado del texto que sacamos del PDF.  
3. Buscar técnicas de chunking más efectivas.  
4. Aunque GPT-3 funciona bastante bien, estaría genial probar con otras opciones como GPT-4 o modelos más específicos, (Incluso Open Weight como Ollama).  
5. Investigar modelos multitarea para hacer que el modelo responda mejor a una variedad de preguntas.  
6. Hacer fine-tuning en el modelo para que sea aún más experto en *Game of Thrones*.  
7. El código actual es monolítico, sería buena refactorizarlo en microservicios.

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
   git clone https://github.com/giulicrenna/Froneus-Challenge
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
   git clone https://github.com/giulicrenna/Froneus-Challenge
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
   git clone https://github.com/giulicrenna/Froneus-Challenge
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
