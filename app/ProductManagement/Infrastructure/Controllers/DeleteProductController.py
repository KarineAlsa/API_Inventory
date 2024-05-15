from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from datetime import datetime
from typing import Any
from ProductManagement.Application.UseCases.DeleteProductUseCase import DeleteProductUseCase

app = FastAPI()

class  DeleteProductController:
    def __init__(self):
        self.use_case = DeleteProductUseCase()

    async def run(self, id:any):
     
        try:
            
            product = await self.use_case.run(id)
            
            if product:
                return {"message": "Producto eliminado", "success": True}
            else:
                raise HTTPException(status_code=400, detail="No se pudo crear el producto.")
        except Exception as error:
            raise HTTPException(status_code=500, detail="Ha ocurrido un error durante su petición.")
