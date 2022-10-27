from fastapi import FastAPI
from pydantic import BaseModel
from emart_model import EMART
import numpy as np
import uvicorn

app = FastAPI()
e = EMART()

class SeoulAirIndex(BaseModel):
    MSRDT_DE : int
    MSRRGN_NM : str
    MSRSTE_NM : str
    O3 : float
    NO2 : float
    CO : float
    SO2 : float
@app.get('/')
async def get():
    return { 'Test' : 'Ok'}


@app.post('/')
async def scoring_endpoint(item:SeoulAirIndex):
    result = e.inference(np.array([item.MSRDT_DE, item.MSRRGN_NM, item.MSRSTE_NM, item.O3, item.NO2, item.CO, item.SO2]))
    return result


if __name__ == '__main__':
    uvicorn.run(app, host = '0.0.0.0', port = 8000)
    