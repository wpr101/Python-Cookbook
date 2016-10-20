class MetaWithArguments(type):
	def __init__(metaclass, name, bases, namespace, **kwargs):
		type.__init__(metaclass, name, bases, namespace)

	def __new__(metaclass, name, bases, namespace, **kwargs):
		for k, v in kwargs.items():
			namespace.setdefault(k, v)

		return type.__new__(metaclass, name, bases, namespace)

class WithArgument(metaclass=MetaWithArguments, spam='eggs'):
	pass

with_argument = WithArgument()
print(with_argument.spam)
