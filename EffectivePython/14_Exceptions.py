'''def divide(a,b):
    try:
        return True, a/b
    except ZeroDivisionError:
        return False, None

x, y = 0, 5
success, result = divide(x,y)
if not success:
    print('invalid inputs')
'''

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from es

x, y = 5, 2
try:
    result = divide(x,y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)
