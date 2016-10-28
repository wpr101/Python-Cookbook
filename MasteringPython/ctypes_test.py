import ctypes

print(ctypes.cdll)
libc = ctypes.cdll.LoadLibrary('libc.so.6')
print(libc)
print(libc.printf)

spam = ctypes.create_string_buffer(b'spam')
print(ctypes.sizeof(spam))
print(spam.raw)
print(spam.value)
print(libc.printf(spam))

format_string = ctypes.create_string_buffer(b'Number: %d\n')
libc.printf(format_string, 123)
x = ctypes.c_int(123)
libc.printf(format_string, x)
