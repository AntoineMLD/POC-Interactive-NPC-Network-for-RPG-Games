# Utiliser une image de base avec Python
FROM python:3.11-slim

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier les fichiers requirements.txt et .env dans le conteneur
COPY requirements.txt ./
COPY .env ./

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers de l'application dans le répertoire de travail du conteneur
COPY . .

# Exposer le port que Streamlit utilisera
EXPOSE 8501

# Définir la commande pour exécuter l'application Streamlit
CMD ["streamlit", "run", "src/streamlit_app.py"]
