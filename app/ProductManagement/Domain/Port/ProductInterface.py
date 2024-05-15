from app.ProductManagement.Domain.Entity.Product import Product

class ProductInterface:
    async def create_product(self, order: Product) -> Product:
        raise NotImplementedError
    
    async def list_all(self) -> list:
        raise NotImplementedError

    async def delete_product(self, id: any) -> Product:
        raise NotImplementedError
