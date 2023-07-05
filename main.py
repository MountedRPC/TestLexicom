import redis
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

redis_client = redis.Redis(host='127.0.0.1', port=6379, db=0)


class Data(BaseModel):
    phone: str
    address: str


@app.post("/write_data")
def write_data(data: Data):
    redis_client.set(data.phone, data.address)
    return {"message": "Data written successfully"}


@app.get("/check_data")
def check_data(phone: str):
    address = redis_client.get(phone)
    if address:
        return {"address": address.decode()}
    else:
        raise HTTPException(status_code=404, detail="Data not found")
