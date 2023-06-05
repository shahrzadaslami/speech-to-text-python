
from happytransformer import HappyTextToText
from happytransformer import TTSettings


#this code will corect your gramatical mistakes

#changes

#latest test
#branch two
happy_tt = HappyTextToText("T5",  "prithivida/grammar_error_correcter_v1")
text = "gec: " + "we no are open tomorrow"
settings = TTSettings(do_sample=True, top_k=10, temperature=0.5,  min_length=1, max_length=100)
result = happy_tt.generate_text(text, args=settings)

print(result.text)
