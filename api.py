import uvicorn
from fastapi import FastAPI
from  pydantic import BaseModel
from TrainerManager import TrainerManager

app = FastAPI()
class userInput(BaseModel):
    name:str
    age:int
@app.get("/")
async def root():
    ui = TrainerManager()
    probability_table,loaded = ui.read_csv()
    if loaded:
        ui.evaluate_model(probability_table)
        return probability_table
    else:
        return {1111111:2222222}


if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)

