from translate import Translator

translator = Translator(to_lang="es")

text = 'hello how are you?'

translation = translator.translate(text)

print("Translated Text: ", translation)