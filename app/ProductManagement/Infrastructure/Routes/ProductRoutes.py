from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from ProductManagement.Infrastructure.Controllers.CreateProductController import CreateProductController
from ProductManagement.Infrastructure.Controllers.ListAllProductController import ListAllProductsUseCase
from ProductManagement.Infrastructure.Controllers.DeleteProductController import DeleteProductController
import asyncio
route = APIRouter()

class ProductRequest(BaseModel):
    Name: str
    Price: float
    Stock: int

@route.post("/")
async def create_product(product: ProductRequest):
    try:
        
        response = await CreateProductController().run(product)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@route.get("/")
async def list_all():
    try:
        
        response = await ListAllProductsUseCase().run()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@route.delete("/{id}")
async def delete(id: int):
    try:
        
        response = await DeleteProductController().run(id)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    