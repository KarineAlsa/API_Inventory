from ProductManagement.Domain.Entity.Product import Product
from ProductManagement.Infrastructure.Repository.InventoryMySQLRepository import ProductMysqlRepository

class   DeleteProductUseCase:
    def __init__(self):
        self.repository = ProductMysqlRepository()

    async def run(self, id:any):
        
        try:
            
            
            await self.repository.delete(id)
            return True
        
        except Exception as error:
            print(f"An error occurred: {error}")
            return None
