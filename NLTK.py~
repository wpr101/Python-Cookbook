import nltk
import re

from nltk.book import *

#text7 is Wall Street Journal
print(text7.concordance("Dow"))
print(text7.similar("up"))
#text7.common_contexts(["monstrous", "very"])
#sorted(set(text3))

def processor(data):
    tokenized=nltk.word_tokenize(data)
    tagged = nltk.pos_tag(tokenized)
    namedEnt = nltk.ne_chunk(tagged, binary=True) 
    print(namedEnt)
    entities = re.findall(r'NE\s(.*?)/', str(namedEnt))
    descriptives = re.findall(r'\(\'(\w*)\',\s\'JJ\w?\'', str(tagged))
    print(entities)
    print(descriptives)


#processor("The sun is shining. The weather is great for taking a walk. William likes to walk in the sun")

#processor("Markets are rising today as the NASDAQ is up 50 points. Apple and Google had good earnings, while GoPro disappointed. Oil stocks were mostly down as OPEC increased production")


