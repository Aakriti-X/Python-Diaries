""" operators are special symbols that help in carrying out an assignment operation or
 arithmetic or logical computation """

# value that operators operates on is called operands

# Python Operators

# 1. Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


# 2. Comparison(Relational) Operators
print("\nComparison Operators:")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)


# 3. Logical Operators
x = True
y = False

print("\nLogical Operators:")
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)


# 4. Assignment Operators
c = 10

print("\nAssignment Operators:")

c += 5
print("c += 5:", c)

c -= 2
print("c -= 2:", c)

c *= 2
print("c *= 2:", c)

c /= 2
print("c /= 2:", c)


# 5. Membership Operators
numbers = [10, 20, 30, 40]

print("\nMembership Operators:")
print("20 in numbers:", 20 in numbers)
print("50 not in numbers:", 50 not in numbers)


# 6. Identity Operators
p = [1, 2, 3]
q = p
r = [1, 2, 3]

print("\nIdentity Operators:")
print("p is q:", p is q)
print("p is r:", p is r)
print("p is not r:", p is not r)