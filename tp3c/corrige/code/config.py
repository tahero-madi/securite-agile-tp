"""Configuration : aucun secret dans le code, tout vient de l'environnement."""
import os

SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE = os.environ.get("DATABASE", "demandes.db")

NOTIF_API_URL = os.environ.get("NOTIF_API_URL", "https://notifications.exemple.local/api/v1")
NOTIF_API_TOKEN = os.environ.get("NOTIF_API_TOKEN")
