from vector import Vector


v = Vector([0.5, 1.0, 2.0, 3.0])
v2 = Vector([1.0, 2.0, 0.5, 5.0])
print(v, v2)
print(v + 5, 5 + v, v + v2, sep=' | ')
print(v - 2, 2 - v, v - v2, sep=' | ')
print(v * 2, 2 * v, v * v2, sep=' | ')
print(v / 2, 2 / v, v / v2, sep=' | ')