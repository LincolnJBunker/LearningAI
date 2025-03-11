from textblob import TextBlob

text = 'Why is the word carousal so hard to spell?'

blob = TextBlob(text)

corrected_text = blob.correct()

print("Original Text: ", text)
print("Corrected Text: ", corrected_text)