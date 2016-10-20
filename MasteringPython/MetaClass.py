# Inheritance of type instead of object
class MetaSpam(type):

	def __new__(metaclass, name, bases, namespace):
		name = 'SpamCreatedByMeta'
		bases = (int,) + bases
		namespace['eggs'] = 1
		return type.__new__(metaclass, name, bases, namespace)

# Meta class
class Spam(object, metaclass=MetaSpam):
	pass

print(Spam.__name__)
print(issubclass(Spam, int))
print(Spam.eggs)
