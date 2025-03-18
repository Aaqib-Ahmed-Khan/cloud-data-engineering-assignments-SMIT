# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Comparison Operators
print("\nComparison Operators:")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)

# Logical Operators
x = True
y = False
print("\nLogical Operators:")
print("AND:", x and y)
print("OR:", x or y)
print("NOT x:", not x)

# Bitwise Operators
p = 5  # 0b0101
q = 3  # 0b0011
print("\nBitwise Operators:")
print("Bitwise AND:", p & q)
print("Bitwise OR:", p | q)
print("Bitwise XOR:", p ^ q)
print("Bitwise NOT (~p):", ~p)
print("Left Shift:", p << 1)
print("Right Shift:", p >> 1)

# Assignment Operators
c = 10
print("\nAssignment Operators:")
c += 5  # c = c + 5
print("c += 5:", c)
c -= 3  # c = c - 3
print("c -= 3:", c)
c *= 2  # c = c * 2
print("c *= 2:", c)
c /= 4  # c = c / 4
print("c /= 4:", c)
c //= 2  # c = c // 2
print("c //= 2:", c)
c %= 3  # c = c % 3
print("c %= 3:", c)
c **= 2  # c = c ** 2
print("c **= 2:", c)

# Identity Operators
m = [1, 2, 3]
n = [1, 2, 3]
print("\nIdentity Operators:")
print("m is n:", m is n)  # False because they are different objects
print("m is not n:", m is not n)  # True

# Membership Operators
text = "Hello Python"
print("\nMembership Operators:")
print("'H' in text:", 'H' in text)
print("'z' not in text:", 'z' not in text)
