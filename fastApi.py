from fastapi import FastAPI
from workflow.workflow import run

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "Hello World"}


@app.post("/infer/{file}")
async def infer(file):
    prediction = await run(file)
    return {"prediction": prediction}
