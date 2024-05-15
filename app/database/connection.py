import mysql.connector
import aiomysql
import os
from dotenv import load_dotenv
load_dotenv()
async def create_connection():
    config = {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'db': os.getenv('DB_NAME')
    }

    try:
        connection = await aiomysql.connect(**config)
        print("Conexión establecida a la base de datos.")  
        return connection
        
    except aiomysql.Error as error:
        print(f"Error al conectar a la base de datos: {error}")
        return None