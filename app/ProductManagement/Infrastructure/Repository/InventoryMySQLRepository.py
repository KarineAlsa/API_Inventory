import aiomysql
import asyncio
import app.ProductManagement.Domain.Entity.Product as Product
from app.database.connection import create_connection as connect
import mysql.connector

class ProductMysqlRepository:
    def __init__(self, pool):
        self.pool = pool

    async def create_product(self, product: Product) -> dict:
        sql = "INSERT INTO Products (Name, Price, Stock) VALUES (%s, %s, %s)"
        params = (product.Name, product.Price, product.Stock)
        db_connection = await connect()
        cursor = await db_connection.cursor()
        if db_connection:
            async with db_connection.cursor() as cursor:
                await cursor.execute(sql, params)
                await db_connection.commit()
                producto = Product(product.Name, product.Price, product.Stock)
                await cursor.close()

            
            return producto
           
        else:
            raise Exception("Error al insertar la orden en la base de datos")

    async def list_all(self) -> list:
        sql = "SELECT * FROM products"
        async with self.pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql)
                result = await cur.fetchall()
                if result:
                    return result
                else:
                    return "No hay órdenes en la base de datos"

