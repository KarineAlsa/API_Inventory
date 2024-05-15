from fastapi import APIRouter, Depends
from pydantic import BaseModel
from ....Dependencies import create_order_controller
import asyncio
route = APIRouter()

class ProductRequest(BaseModel):
    Name: str
    Price: float
    Stock: int

@route.post("/")
async def create_product(product: ProductRequest):
    try:
        response = await create_order_controller.run(create_order_controller)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))