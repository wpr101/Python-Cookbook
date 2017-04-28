import nltk 
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
print(tokenizer.tokenize("Have a nice day. I hope you find the book interesting"))

text = nltk.word_tokenize(" Don't hesitate to ask questions")
print(text)

from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()
print(tokenizer.tokenize(" Don't hesitate to ask questions"))

