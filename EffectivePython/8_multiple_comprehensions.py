matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat = [x for row in matrix for x in row]
print(flat)

squared = [[x**2 for x in row] for row in matrix]
print(squared)

a = [1,2,3,4,5,6,7,8,9,10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]

filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]

print(filtered)
