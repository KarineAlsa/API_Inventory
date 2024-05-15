from app.ProductManagement.Domain.Entity.Product import Product

class CreateProductUseCase:
    def __init__(self, repository):
        self.repository = repository

    async def run(self, Name: str, Price: float, Stock: int):
        try:
            product = Product(Name, Price, Stock)
            return await self.repository.create_order(product)
        except Exception as error:
            print(f"An error occurred: {error}")
            return None
