# MongoDB standalone server

Exemple d'utilisation d'un serveur MongoDB en standalone.

## Prérequis

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3](https://www.python.org/)

## Installation

Installer les packages python nécessaires

```bash
pip install -r requirements.txt
```

Lancer MongoDB avec docker compose

```bash
docker-compose up -d
```

## Utilisation

Lancer le script python

```bash
python main.py
```