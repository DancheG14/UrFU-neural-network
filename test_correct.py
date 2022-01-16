pip install pytest
pip install happytransformer

from happytransformer import HappyTextToText, TTSettings
import requests
import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")

args = TTSettings(num_beams=5, min_length=1)

text = 'grammar: This sentence has has bads grammar!'
# Add the prefix "grammar: " before each input
result = happy_tt.generate_text(f'{text}.', args=args)

print(result.text) # This sentence has bad grammar.


def correct(text):
  response = client.post("/correct/",
    json={"text": "grammar: This sentence has has bad grammar!"}
    )
    json_data = response.json() 

  assert response.status_code == 200
  result = happy_tt.generate_text(f'{json}.', args=args)
  return result.text

def test_uncorrect(text2):
  response = client.post("/correct/",
    json={"text": "grammar: This sentence has bad grammar!"}
    )
    json_data = response.json()
  result2 = happy_tt.generate_text(f'{json}.', args=args)
  return result2.text2
  assert response.status_code == 200

text = "grammar: This sentence has bad grammar!"
text2 = "grammar: This sentence has has bads grammar!"

result = correct(text)
result2 = correct(text2)
	
