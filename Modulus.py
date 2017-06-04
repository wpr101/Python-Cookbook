
def powers():
    powers_list = []
    for i in range(10):
        if i % 2 == 0:
            powers_list.append(i*i)

    return powers_list
    
print(powers())
