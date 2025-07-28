import uvicorn
from fastapi import FastAPI
from  pydantic import BaseModel
from StatisticsManager import StatisticsManager
from Statistics_by_data import StatisticsByData

app = FastAPI()
class userInput(BaseModel):
    name:str
    age:int
@app.get("/")
async def root():
    ui = StatisticsManager()
    probability_table = ui.read_csv()
    ui.evaluate_model(probability_table)
    return probability_table


if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)

