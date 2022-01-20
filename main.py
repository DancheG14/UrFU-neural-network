from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()

classifier = pipeline("sentiment-analysis", "blanchefort/rubert-base-cased-sentiment")

print(classifier("Привет! Как дела?"))
print(classifier("Привет! Я убью тебя лодочнин!"))
print(classifier("Привет! Я люблю тебя!"))

@app.get("/")
def root():
    return {"message": "Hello UrFU"}

@app.post("/predict/") 
def predict(item: Item):
    return classifier(item.text)[0]

