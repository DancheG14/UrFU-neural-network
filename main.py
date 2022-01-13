from fastapi import FastAPI
from happytransformer import HappyTextToText, TTSettings
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()
happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
args = TTSettings(num_beams=5, min_length=1)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/predict/")
def predict(item: Item):
      return happy_tt.generate_text(f'{item.text}.', args=args).text

