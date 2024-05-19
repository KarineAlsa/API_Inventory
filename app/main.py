from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import connection
import threading
from ProductManagement.Infrastructure.Services.rabbit import consume_messages
from ProductManagement.Infrastructure.Routes.ProductRoutes import route 
from dotenv import load_dotenv
load_dotenv()
import uvicorn
app = FastAPI()
app.include_router(route)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def shutdown_event():
    if connection.db_connection:
        connection.db_connection.close()
        connection.cursor.close()
        print("Conexión a la base de datos cerrada.")

rabbitmq_thread = threading.Thread(target=consume_messages)
rabbitmq_thread.start()

if __name__ == "__main__":  
    uvicorn.run(app,port=8080)