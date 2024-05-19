from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from datetime import datetime
from typing import Any
from ProductManagement.Application.UseCases.UpdateStockOrderSentUseCase import UpdateStockOrderSentUseCase

app = FastAPI()

class  UpdateStockOrderSentController:
    def __init__(self):
        self.use_case = UpdateStockOrderSentUseCase()

    def run(self, products:any):
     
        try:
            
            product = self.use_case.run(products)
            
            
            if product:
                print("Stock actualizado")
                return True
            else:
                raise HTTPException(status_code=400, detail="No se pudo crear el producto.")
        except Exception as error:
            raise HTTPException(status_code=500, detail="Ha ocurrido un error durante su petición.")
