from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from datetime import datetime
from typing import Any
from ProductManagement.Application.UseCases.CreateProductUseCase import CreateProductUseCase

app = FastAPI()

class ProductRequest(BaseModel):
    Name: str
    Price: float
    Stock: int

class CreateProductController:
    def __init__(self):
        self.use_case = CreateProductUseCase()

    async def run(self, request: ProductRequest):
        Name = request.Name
        Price = request.Price
        Stock = request.Stock
        
        
        if not Name or not Price or not Stock:
            raise HTTPException(status_code=400, detail="Debe completar todos los campos.")

        if Price < 0:
            raise HTTPException(status_code=400, detail="Precio no puede ser negativo.")
        

        try:
            
            product = await self.use_case.run(Name, Price, Stock)
            
            if product:
                return {"data": product, "message": "Producto creado", "success": True}
            else:
                raise HTTPException(status_code=400, detail="No se pudo crear el producto.")
        except Exception as error:
            raise HTTPException(status_code=500, detail="Ha ocurrido un error durante su petición.")
