# Usa una imagen base de Python
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY . .

RUN rm -f .env

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8082

CMD ["streamlit", "run", "main.py", "--server.port=8082", "--server.address=0.0.0.0"]