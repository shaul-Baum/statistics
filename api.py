import  uvicorn
from fastapi import FastAPI
from  pydantic import BaseModel
# import Statistics_input
from UserInteraction import UserInteraction

app = FastAPI()
class userInput(BaseModel):
    name:str
    age:int
@app.get("/{colom}")
async def root(colom):
    a = colom.split(",")
    ui = UserInteraction()
    ui.read_csv()
    ui.evaluate_model(ui)
    ui.update_statistics(a[0],a[1])
    statistics,statistics_v =  ui.finalize_scores()
    return {statistics : statistics_v}
# @app.post("/")
# async def greet(user:userInput):
#     return

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)

