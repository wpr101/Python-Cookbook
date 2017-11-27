'''enable_tracing = True
if enable_tracing:
    #debug_log = open("debug.log", "w")

def trace(func):
    if enable_tracing:
        def callf(*args, **kwargs):
            print("func.__name__: " + func.__name__)
            print("args: " + str(args))
            print("kwargs: " + str(kwargs))
            debug_log.write("Calling %s: %s, %s\n" % (func.__name__, args, kwargs))
            r = func(*args, **kwargs)
            debug_log.write("%s returned %s\n" % (func.__name__, r))
            return r
        return callf
    else:
        return func

@trace
def square(x, y=10):
    return x*x

square(4)'''

'''def debug(func):
    def wrapped(*args, **kwargs):
        print("args: " + str(args))
        print("kwargs: " + str(kwargs))
        print("Calling: " + func.__name__)
        r = func(*args, **kwargs)
        print("Done calling: " + func.__name__)
        return r
    return wrapped

@debug
def add(x,y,z):
    return x + y + z

print(add(2, y=4, z=5))'''


event_handlers = { }
def eventhandler(event):
    print("event: " + event)
    def register_function(f):
        print("here")
        event_handlers[event] = f
        return f
    return register_function

@eventhandler('BUTTON')
def handle_button(msg):
    pass

#@eventhandler('RESET')
#def handle_reset(msg):
    #print('Reset message')

temp = eventhandler('BUTTON')
handle_button = temp(handle_button)
print(str(event_handlers))
