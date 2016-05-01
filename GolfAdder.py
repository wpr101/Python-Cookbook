def adder(a,b):
 return format(int(a,2)+int(b,2),'b').zfill(4)
 #return bin(int(a,2)+int(b,2))
print(adder("0001", "0001"))
