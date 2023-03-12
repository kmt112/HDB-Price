from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import random
from pydantic import BaseModel
from typing import Union
from Xformer import transform, get_shortest_distance

class Item(BaseModel):
    town: str
    flat_type: str
    floor_area_sqm: float
    flat_model: str
    remaining_lease: float
    storey: float
    address_name: str
    # shortest_mrt_distance: float
    # shortest_primary_distance: float
    # shortest_cbd_distance: float

app = FastAPI()


@app.get('/')
async def root():
    return {'example':'This is an example','data':999}

@app.get('/random')
async def get_random():
    rn: int=random.randint(0,100)
    return {'number': rn , 'limit':100}

@app.post("/predict/")
async def create_item(item: Item):
    #getting address
    address_name = item.address_name
    shortest_cbd_area, shortest_primary_distance, shortest_mrt_distance = get_shortest_distance(address_name)
    json_compatible_item_data = jsonable_encoder(item)
    predicted_price = transform(json_compatible_item_data,shortest_cbd_area, shortest_primary_distance, shortest_mrt_distance)
    # transform(item)
    return predicted_price.tolist()

