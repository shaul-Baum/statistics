import  uvicorn
from fastapi import FastAPI
from  pydantic import BaseModel
import Statistics_input

app = FastAPI()
class userInput(BaseModel):
    name:str
    age:int
@app.get("/{colom}/{itam}")
async def root(colom,itam):
    r =Statistics_input.StatisticsInterface()
    r.read_csv()
    statistics,statistics_v = r.update_statistics(colom,itam)
    statistics_v = int(statistics_v * 100)
    return f"yor statistic is: {statistics} {statistics_v}%"
@app.post("/")
async def greet(user:userInput):
    return

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)

