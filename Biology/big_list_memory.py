import psutil, os

def print_mem():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / 1000
    print("Used this much memory: " + str(mem))

l = set(range(1000000))
print_mem()

def number_in_list():
    return 12345 in l
