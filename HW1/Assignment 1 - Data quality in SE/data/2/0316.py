from numpy import array, linalg, matmul

a = array([[1, -1, 0], [3, 0, -1], [1, 3, -2]])
print(a)

b = array([[2, -1, 1], [0, 3, -1], [-1, 2, 0]])
print(b)


inv = linalg.inv(a)
print(inv)


i = linalg.inv(b)
print(i)


ab = matmul(a, b)
print(ab)
