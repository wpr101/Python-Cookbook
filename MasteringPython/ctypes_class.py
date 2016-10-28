import ctypes

class Spam(ctypes.Structure):
	_fields_ = [
		('spam', ctypes.c_int),
		('eggs', ctypes.c_double),
	]

spam = Spam(123, 456.789)
print(spam.spam)
print(spam.eggs)

Spams = 5 * Spam
spams = Spams()
spams[0].eggs = 123.456
print(spams)
print(spams[0])
print(spams[0].eggs)
print(spams[0].spam)

