# Python input function

from keyword import kwlist

from getpass import getpass

print(kwlist)

name = input("Enter your name: ")

print(f"Your name is {name}")

print("Your name is", name)

passw = getpass("Enter pass: ")
print(passw)




