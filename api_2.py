import uvicorn
from fastapi import FastAPI
from  pydantic import BaseModel
from Validator import Validator
import requests
import json

app = FastAPI()
class userInput(BaseModel):
    name:str
    age:int
@app.get("/{colom_value}")
async def root(colom_value):
    a = colom_value.split(",")
    response = requests.get("http://api:8000")
    if response.status_code == 200:
        probability_table =response.json()
        e = Validator(probability_table)
        if len(a)>=2:
            e.update_statistics(a[0],a[1])
            statistics,statistics_v =  e.finalize_scores()
            return {statistics : statistics_v}
    else:
        print(response.statos_code)
        return response.statos_code


if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)

