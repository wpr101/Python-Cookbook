# Same definition as below
# class Spam(object):
	#eggs = 'my eggs'

# Same definition as above
Spam = type('Spam', (object,), dict(eggs='my eggs'))

spam = Spam()
print(spam.eggs)
print(type(spam))
print(type(Spam))

