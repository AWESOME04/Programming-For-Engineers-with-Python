# Python arithmetic operations + - * / // % **
x = 2

y = 3
# Addition +
print(x + y)

# Subtraction -
print(x - y)

# Multiplication *
print(x * y)

# Division /
print(x / y)

# Floor Division // - # Data type is an int
print(x // y)

# Power **
print(x ** y)

# Modulus %
print(x % y)

# Order of precedence-> (BODMAS)


# Math functions


# round
print(round(x/ y, 2))

# absolute value
i = -18
print(abs(i))

# Exercise
num_1 = int(input("Enter first value:\n"))
num_2 = int(input("Enter second value:\n"))

result = num_1 % num_2

output = f"The mod of {num_1} mod {num_2} = {result}"

print(output)

# For any operator
num1 = int(input("Enter first value: \n"))
num2 = int(input("Enter second value: \n"))
op = input("Enter operator(+, -, *, /, //, %): \n")

if op == "+":
    result = num1 + num2
    print(f"The result is {result}")
elif op == "-":
    result = num1 - num2
    print(f"The result is {result}")
elif op == "*":
    result = num1 * num2
    print(f"The result is {result}")
elif op == "/":
    result = num1 / num2
    print(f"The result is {result}")
elif op == "//":
    result = num1 // num2
    print(f"The result is {result}")
elif op == "%":
    result = num1 % num2
    print(f"The result is {result}")
else:
    print("Please enter a valid operator(+, -, *, /, //, %)")


# Program to calculate the Area of a circle - pi*r**2
radius = int(input("Enter the radius of the circle: \n"))

