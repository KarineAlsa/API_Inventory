from ProductManagement.Domain.Entity.Product import Product
from ProductManagement.Infrastructure.Repository.InventoryMySQLRepository import ProductMysqlRepository

class UpdateStockOrderSentUseCase:
    def __init__(self):
        self.repository = ProductMysqlRepository()

    def run(self, products:any):
        
        try:
            
            self.repository.update_stock(products)
            return True
        
        except Exception as error:
            print(f"An error occurred: {error}")
            return None
