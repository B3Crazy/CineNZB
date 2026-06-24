FROM python:3.11-slim

# Arbeitsverzeichnis
WORKDIR /app

# Systemabhängigkeiten für watchdog
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Requirements installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Projekt kopieren
COPY app/ ./

    # Config-Verzeichnis erstellen
RUN mkdir -p /config
VOLUME ["/config"]

# Port (optional, aber sauber)
EXPOSE 2160

# Startbefehl
CMD ["python", "main.py"]
