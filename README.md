# 📘 CineNZB

## 🚀 Overview
CineNZB is a lightweight NZB management tool featuring:

- Automatic folder watching (Linux‑optimized)
- Recursive NZB library scanning
- Persistent SQLite database
- REST API
- Optional Web UI
- Full Docker support for easy deployment

The application is optimized for Linux hosts.
Due to Docker Desktop limitations, real‑time file watching is not reliable on Windows.

---

## 🐳 Installation (Docker Compose)

Example docker-compose.yml:

```yaml
    version: "3.9"

    services:
      cinenzb:
        image: deinname/cinenzb:latest
        container_name: cinenzb
        ports:
          - "5000:5000"
        volumes:
          - "/path/to/nzb/library:/nzbs"
          - "/path/to/config:/config"
        restart: unless-stopped
```

Start the service:

    docker compose pull
    docker compose up -d

Stop the service:

    docker compose down

---

## 📁 Directory Structure

CineNZB uses two main directories:

| Path | Purpose |
|------|---------|
| /nzbs | Your NZB library (Movies, Series, etc.) |
| /config | Persistent configuration and database files |
| /config/library.db | SQLite database |
| /config/settings.json | Future application settings |
| /config/users.json | Future user accounts |
| /config/logs/ | Log files |

All data inside /config is persistent and survives container updates.

---

## ⚙️ Configuration

Supported environment variables:

| Variable | Default | Description |
|----------|----------|-------------|
| CONFIG_DIR | /config | Directory for DB & settings |
| HOST | 0.0.0.0 | Bind address for the API |
| PORT | 5000 | API port |

Example:

    environment:
      - CONFIG_DIR=/config
      - HOST=0.0.0.0
      - PORT=5000

---

## 🧱 Database

CineNZB uses SQLite and automatically creates the database on startup if it does not exist.

The database is stored in:

    /config/library.db

This ensures:

- Data persists across updates
- Users can back up or migrate easily
- The image remains stateless and portable

---

## 🔍 File Watching

CineNZB includes a real-time file watcher for NZB imports.

Fully supported:

- Linux hosts
- Docker on Linux
- WSL2 mounts
- Docker volumes

Not reliable:

- Windows host paths mounted into Docker Desktop
  (Docker Desktop does not forward inotify events)

If running on Windows, use manual scanning or periodic scanning.

---

## 🛠 Development Setup

Clone the repository:

    git clone https://github.com/yourname/cinenzb.git
    cd cinenzb

Install dependencies:

    pip install -r requirements.txt

Run locally:

    python main.py

---

## 🐳 Building the Docker Image

    docker build -t deinname/cinenzb:latest .
    docker push deinname/cinenzb:latest

---

## 📄 License

MIT License (or your chosen license).

---

## 🙌 Contributing

Pull requests are welcome.
Please open an issue first to discuss major changes.
