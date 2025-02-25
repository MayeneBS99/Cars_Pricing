FROM python:3.9-slim

# repertoire de travail
WORKDIR /API

# copie du requirements dans le conteneur
COPY requirements.txt .

# installer les dependances
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
COPY API/ ./API

EXPOSE 8000

# demarer le serveur FastAPI avec uvicorn
CMD ["uvicorn", "src.API.main:app", "--host", "0.0.0.0", "--port", "8000"]