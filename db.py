import os
import mysql.connector

def get_connection():
    # Conectamos usando las variables de entorno
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),       # Host de Railway
        port=int(os.environ.get("DB_PORT", 3306)),         # Puerto de Railway
        user=os.environ.get("DB_USER", "root"),           # Usuario
        password=os.environ.get("DB_PASSWORD", ""),       # Contraseña
        database=os.environ.get("DB_NAME", "flask_db")    # Base de datos
    )