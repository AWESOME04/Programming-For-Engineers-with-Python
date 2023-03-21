# A function is a block of reusable code
# Place a parenthesis() in front of the function name to call / invoke it

def my_function(name, age):
    print("Happy are we. Studios are we...")
    print("This is my function")
    print(f"My name is {name}, I am {age} years old")

my_function("Kwame Nkrumah", "34")

def addition(x, y, *args, **kwargs):
    print("x = ", x)
    print("y = ", y)
    print("args = ", args)
    print("kwargs = ", kwargs)

addition(10, 9, 9, 2, name="John", age=70)


# Changing the default order
def myFunc(x, y):
    print(x)
    print(y)

myFunc(y=6, x=7)



def sum_or_even():
    num = int(input("Enter a number \n"))
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

sum_or_even()

def addition(**kwargs):
    print(kwargs)
    print(type(kwargs))

addition(name="John", level=200, age=50)


*x, y = 2, 4, 5, 6,7

print(type(x))
print(type(y))
print(x)
print(y)

# Functions for Arithmetic Operations with the return keyword
# The return keyword does not print any output

# Note that the print is only accessible in sys.out

def addition(x, y):
    z = x + y
    return f"Sum = {z}"

print(addition(2, 3))

def subtraction(x, y):
    z = x - y
    return f"Difference = {z}"

print(subtraction(2, 3))

def product(x, y):
    z = x * y
    return f"Product = {z}"

print(product(2, 3))

def division(x, y):
    z = x / y
    return f"Sum = {z}"

print(division(2, 3))


# Calling the function
# my_function()

# for i in range(5):
#     my_function()

def sample():
    return "Awesomeness"

print(sample())

def name_func(name="Evans", age = 12):
    return f"{name} is pretty AWESOME!, {age} is my football age"

print(name_func())


def add(x, *y):
    # z = x + y
    print(x)
    print(y)
    # return f"Sum = {z}"

add(3, 8, 2, 3, 4)

def empty():
    pass


# Parameters vs Argument
# A parameter is the variable listed inside the parentheses in the function definition.



# An argument is the value that is sent to the function when it is called.


# Functions with Parameters and Argument
def myfunc(name, age):
    print(f"My name is {name}")
    print(f"I am {age} years old.")

names = ["Jane", "John", "Mark", "Joshua"]
ages = [19, 20, 21, 22]
for name, age in zip(names, ages):
    myfunc(name, age)

# Important to be mindful of indentation


# *args and **kwargs
# *args : - Non keyword arguments...type: - List

# **kwargs : - Keyword arguments...type: - Dict

# Using the multiple assignment operator

def addition(*args):
    print(args)
    print(type(args))

print(addition(3, 2, 3, 4, 5, 6, 7))
# Data type of x is a tuple

x, *y = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(y)
print(type(y))

# *args
def addition(*args):
    total = 0
    for numbers in args:
        total += numbers
    print(f"Sum = {total}")

addition(1, 2, 3, 4, 5, 6, 7, 8, 9)

# **kwargs
# Note: kwargs can be used to obtain specific things
def myFunc(*args, **kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(kwargs.get("name"))
    for keys, values in kwargs.items():
        print(f"{keys} = {values}")

    print(type(kwargs))

myFunc("Ghana", "University of Ghana", name="Kwame", age=20)

