import spacy

nlp = spacy.load('en')

doc1 = nlp(u'the fries were gross')
doc2 = nlp(u'worst fries ever')
doc3 = nlp(u'the fries were excellent')
print(doc1.similarity(doc2))
print(doc1.similarity(doc3))
