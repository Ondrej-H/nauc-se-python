
ix, ocko = 'xo'
print(ix)       # vytiskne 'x'
print(ocko)     # vytiskne 'o'

jedna, dva, tri = [1, 2, 3]
print(jedna)
print(dva)
print(tri)
print(30* "-")

def podil_a_zbytek(a, b):
    return a // b, a % b

podil, zbytek = podil_a_zbytek(12, 5)
print(podil)
print(zbytek)