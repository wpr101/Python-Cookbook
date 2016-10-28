import cffi

ffi = cffi.FFI()
ffi.cdef('''
	typedef struct {
		int x;
		int y;
	} point;

	typedef struct {
		point a;
		point b;
		point c;
	} vertex;
''')

vertices = ffi.new('vertex[]', 5)
v = vertices[0]
v.a.x = 1
v.a.y = 2
v.b.x = 3
v.b.y = 4
v.c.x = 5
v.c.y = 6
print(v.a.x, v.a.y, v.b.x, v.b.y, v.c.x, v.c.y)

# Arrays
x = ffi.new('int[10]')
y = ffi.new('int[]', 10)
x[0:10] = range(10)
y[0:10] = range(10, 0, -1)
print(list(x))
print(list(y))
