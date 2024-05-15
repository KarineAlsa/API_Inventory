from ProductManagement.Domain.Entity.Product import Product
from ProductManagement.Infrastructure.Repository.InventoryMySQLRepository import ProductMysqlRepository

class ListAllProductsUseCase:
    def __init__(self):
        self.repository = ProductMysqlRepository()

    async def run(self):
        
        try:
            
            product = await self.repository.list_all()
            return {"data": product, "message": "Productos obtenidos", "success": True}
        
        except Exception as error:
            print(f"An error occurred: {error}")
            return None
