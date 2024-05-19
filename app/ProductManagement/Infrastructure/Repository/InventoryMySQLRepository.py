import aiomysql
import asyncio
import ProductManagement.Domain.Entity.Product as Product
from database.connection import create_connection as connect
from database.connection import create_connection_sync as connect_sync
import mysql.connector

class ProductMysqlRepository:
    def __init__(self):
        self.pool = None

    async def create_product(self, product: Product) -> dict:
        sql = "INSERT INTO Products (Name, Price, Stock) VALUES (%s, %s, %s)"
        params = (product.Name, product.Price, product.Stock)
        db_connection = await connect()
        cursor = await db_connection.cursor()
        if db_connection:
            async with db_connection.cursor() as cursor:
                
                await cursor.execute(sql, params)
                await db_connection.commit()
                
                await cursor.close()

            return {
                "Name": product.Name,
                "Price": product.Price,
                "Stock": product.Stock
            }
           
        else:
            raise Exception("Error al insertar la orden en la base de datos")

    async def list_all(self) -> list:
        sql = "SELECT * FROM Products"
        
        db_connection = await connect()
        cursor = await db_connection.cursor()
        
        if db_connection:
            async with db_connection.cursor() as cursor:
                await cursor.execute(sql)
                await db_connection.commit()
                result = await cursor.fetchall()
                if result:
                    products = []
                    for row in result:
                        product_dict = {
                            "Id": row[0],
                            "Name": row[1],
                            "Price": row[2],
                            "Stock": row[3]
                        }
                        products.append(product_dict)
                    return products
                else:
                    return "No hay órdenes en la base de datos"
        else:
            raise Exception("Error al conectar con la base de datos")
        
    async def delete(self,id: any):
        sql = "DELETE FROM Products WHERE id = %s;"
        params = (id)
        db_connection = await connect()
        cursor = await db_connection.cursor()
        
        if db_connection:
            async with db_connection.cursor() as cursor:
                await cursor.execute(sql, params)
                await db_connection.commit()
                
                await cursor.close()
                return True
        
        else:
            raise Exception("Error al conectar con la base de datos")
        
    def update_stock(self, products: any):
        db_connection = connect_sync()
        
        if db_connection:
            with db_connection.cursor() as cursor:
                for product in products:
                    product_id = int(product['product_id'])
                    quantity_sold = int(product['total_quantity'])
              
                    current_stock = self.get_stock(product_id, db_connection)
      
                    new_stock = current_stock - quantity_sold
                    
                    sql = "UPDATE Products SET Stock = %s WHERE id = %s;"
                    params = (new_stock, product_id)
                    cursor.execute(sql, params)
                
                db_connection.commit()
                cursor.close()
                return True
        else:
            raise Exception("Error al conectar con la base de datos")
    
    def get_stock(self, id: int, db_connection):
        sql = "SELECT Stock FROM Products WHERE id = %s;"
        params = (id)
        
        with db_connection.cursor() as cursor:
            cursor.execute(sql, params)
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                raise Exception(f"No se encontró el producto con id {id}")