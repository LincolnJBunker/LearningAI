import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sample_text = 'Life is like a box of chocolates you never know what you are going to get!'
tokens = word_tokenize(sample_text)

unigrams = list(ngrams(tokens, 1))
print('Unigrams:', unigrams)

bigrams = list(ngrams(tokens, 2))
print('Bigrams:', bigrams)      

trigrams = list(ngrams(tokens, 3))
print('Trigrams:', trigrams)