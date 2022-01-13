from happytransformer import HappyTextToText, TTSettings

happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")

args = TTSettings(num_beams=5, min_length=1)
text = input()
# Add the prefix "grammar: " before each input
result = happy_tt.generate_text(f'{text}.', args=args)

print(result.text) # This sentence has bad grammar.


def correct(text):
  result = happy_tt.generate_text(f'{text}.', args=args)
  return result.text

def test_uncorrect(text2):
  result2 = happy_tt.generate_text(f'{text2}.', args=args)
  return result2.text2

text = "This sentence has bad grammar!"
text2 = "This sentence has has bads grammar!"

result = correct(text2)
result2 = correct(text2)

assert result == text
assert result2 == text2
