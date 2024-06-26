from ProductManagement.Domain.Entity.Product import Product
from ProductManagement.Infrastructure.Repository.InventoryMySQLRepository import ProductMysqlRepository

class CreateProductUseCase:
    def __init__(self):
        self.repository = ProductMysqlRepository()

    async def run(self, Name: str, Price: float, Stock: int):
        
        try:
            product = Product(Name=Name, Price=Price, Stock=Stock)
            
            return await self.repository.create_product(product)
        
        except Exception as error:
            print(f"An error occurred: {error}")
            return None
