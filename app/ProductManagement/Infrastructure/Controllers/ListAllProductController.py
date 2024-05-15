from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from datetime import datetime
from typing import Any
from ProductManagement.Application.UseCases.ListAllProductsUseCase import ListAllProductsUseCase

app = FastAPI()

class CreateProductController:
    def __init__(self):
        self.use_case = ListAllProductsUseCase()

    async def run(self):

        try:
            
            product = await self.use_case.run()
            
            if product:
                return {"data": product, "message": "Productos traidos", "success": True}
            else:
                raise HTTPException(status_code=400, detail="No se pudo traer productps.")
        except Exception as error:
            raise HTTPException(status_code=500, detail="Ha ocurrido un error durante su petición.")
