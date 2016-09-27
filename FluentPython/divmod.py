print(divmod(20,8))

t = (20,8)
print(divmod(*t))

quotient, remainder = divmod(*t)
print(quotient, remainder)
