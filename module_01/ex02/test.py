from vector import Vector

# Column vector of shape n * 1
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5

print(v2)
# Expected output:
# Vector([[0.0], [5.0], [10.0], [15.0]])
# Row vector of shape 1 * n
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1 * 5
print(v2)
# Expected output
# Vector([[0.0, 5.0, 10.0, 15.0]])
v2 = v1 / 2.0
print(v2)
# Expected output
# Vector([[0.0], [0.5], [1.0], [1.5]])
v1 / 0.0

# Expected ouput
# ZeroDivisionError: division by zero.
2.0 / v1
# Expected output:
# NotImplementedError: Division of a scalar by a Vector is not defined here.

dot = v1.dot(v2)
print(dot)
# Expected output:
# 7.0

print(v1 + v2)
# Expected output:
# Vector([[0.0], [1.5], [3.0], [4.5]])

print(v1 - v2)
# Expected output:
# Vector([[0.0], [0.5], [1.0], [1.5]])

try:
    test = Vector("lol")
except AssertionError as e:
    print("AssertionError:", e)
# Expected output:
# TypeError: Invalid initializer

try:
    test = Vector([[1, 2], [3, 4]])
except AssertionError as e:
    print("AssertionError:", e)
# Expected output:
# AssertionError: Vector must be a row or a column

try:
    v1 * "lol"
except AssertionError as e:
    print("AssertionError:", e)
# Expected output:
# TypeError: other must be a number

try:
    v1 / "lol"
except AssertionError as e:
    print("AssertionError:", e)
# Expected output:
# TypeError: other must be a number

try:
    v1 + "lol"
except AssertionError as e:
    print("AssertionError:", e)
# Expected output:
# TypeError: other must be a Vector

try:
    v1 - "lol"
except AssertionError as e:
    print("AssertionError:", e)
# Expected output:
# TypeError: other must be a Vector

v2 = Vector(20)
print(v2)
# Expected output:
# Vector([
#   [0.0], [1.0], [2.0], [3.0], [4.0], [5.0], [6.0],
#   [7.0], [8.0], [9.0], [10.0], [11.0], [12.0], [13.0],
#   [14.0], [15.0], [16.0], [17.0], [18.0], [19.0]
# ])

v2 = Vector((20, 1))
print(v2)
# Expected output:
# Vector([
#   [19.0], [18.0], [17.0], [16.0], [15.0], [14.0], [13.0],
#   [12.0], [11.0], [10.0], [9.0], [8.0], [7.0], [6.0],
#   [5.0], [4.0], [3.0], [2.0], [1.0]
# ])
