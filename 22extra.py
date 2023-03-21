# Exception Handling
import sys
import os

try:
    name = "Kwame"
    print(name)
except:
    print("Error: Variable not defined")

num_1 = int(input("Number 1: "))
num_2 = int(input("Number 2: "))

try:
    result = num_1 / num_2
except ZeroDivisionError:
    print("Error: Cannot Divide by zero")
    sys.exit(1)
finally:
    print("Code executed successfully")
print(f"Division: {result}")

# Environment Variables
secret_key = "my_secret_key@+190123"
token = "233k3i3oxocdj393j3j22"
password = "123456789"

key = os.environ.get("secret_key")
my_password = os.environ.get("password")
my_token = os.environ.get("token")
print(key)
print(my_password)
print(my_token)

# Virtual Environment in Python

















