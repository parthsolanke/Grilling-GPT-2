from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import requests

app = FastAPI()

API_URL = "https://api-inference.huggingface.co/models/parthsolanke/saul-gpt2-mk2"
HEADERS = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}


class QueryInput(BaseModel):
    query: str


def query_model(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()


def preprocess(query):
    return "<s> " + query + " <bot>: "


@app.post("/query")
def handle_query(query_input: QueryInput = Body(...)):
    processed_query = preprocess(query_input.query)
    model_output = query_model({"inputs": processed_query})
    return {"response": model_output["generated_text"]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
