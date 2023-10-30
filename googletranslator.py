import googletrans
from googletrans import Translator

print(googletrans.LANGUAGES)
from googletrans import Translator

translator = Translator()
result = translator.translate("salut programatori ")
print(result)

result = translator.translate("salut programatori", src="ro", dest="en")
print(result)


text1 = """
हैलो पायथन प्रोग्रामर्स
"""
text2 = """
how are you
"""
translator = Translator()

lang1 = translator.detect(text1)
print(lang1)
lang2 = translator.detect(text2)
print(lang2)
