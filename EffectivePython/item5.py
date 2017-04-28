#item5
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#print('First four:', a[:4])
#print('Last four:', a[-4:])
#print('Middle two:', a[3:-3])

#leave out the zero to reduce noise
assert a[:5] == a[0:5]
assert a[5:] == a[5:len(a)]

'''
print(a[:])
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])
'''

first_twenty_items = a[:20]
last_twenty_items = a[-20:]

#print(a[20])

b = a[4:]
print(b)

b[1] = 99
print(b)

print(a)

a[2:7] = [99, 22, 14]
print(a)

b = a[:]
print(b)
assert b == a and b is not a

b = a
print(a)
a[:] = [101, 102, 103]
assert a is b
print (a) 
