# Python conditional statement if else elif
# isnumeric only applies to strings and not to ints

# EXERCISE

# Program takes two inputs and checks which of the inputs is greater
num1 = int(input("Enter first value: \n"))
num2 = int(input("Enter second value: \n"))

if num1 > num2:
    print("First value is greater than the second value")
elif num2 > num1:
    print("Second value is greater than the first value ")
else:
    print("The numbers are equal")

# Check Odd or Even numbers
num_check = int(input("Enter a number: \n"))

if num_check % 2 == 0:
    print("The number is even")
elif num_check % 2 == 1:
    print("The number is odd")

# Grade check results:
grade = int(input("Enter your score: \n"))
if grade >= 90:
    print("You had an A")
elif 80 <= grade < 90:
    print("You had a B")
elif 70 <= grade < 80:
    print("You had a C")
elif 60 <= grade < 70:
    print("You had a D")
elif 50 <= grade < 60:
    print("You had a E")
else:
    print("You had an F.")

# User input score and grade displays in the terminal
voting_age = 18
age = input('Enter your age: \n')
if age.isnumeric():
    if int(age) >= voting_age:
        print("You are qualified to vote")
    elif int(age) < voting_age:
        print("You are not qualified to vote")
else:
    print("Invalid input.")


#












