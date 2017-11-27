from urllib import urlopen
def page(url):
    def get():
        return urlopen(url).read()
    return get

python = page("http://www.python.org")
jython = page("http://www.jython.org")
print(python.__closure__)
print(python.__closure__[0].cell_contents)

pydata = python()
print(pydata)
