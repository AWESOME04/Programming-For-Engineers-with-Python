# Python dictionary is a collection of key value a pair of data.
# It is ordered and mutable.
# It allows duplicate members

fruits = ["mango", "apple", "strawberry"]
fruits[1] = "pineapple"
print(fruits)

print("")

# Dictionary Methods
student_info = {
    "Name": "Kenneth",
    "Age": 20,
    "Level": 200,
    "Email": "ken@student.com"
}

print(student_info)
print(type(student_info))
print("")

student_info["Level"] = 300
student_info["Email"] = "den@student.com"
student_info["Name"] = "Den"
print(student_info)

print("")
# Copy -- Returns a copy of the dictionary
student_info_copy = student_info.copy()
print(student_info)

print("")
# Keys -- Returns a list containing the dictionary's keys
for key in student_info:
    print(key)

# ALT
print(student_info.keys())


print("")
# Clear -- Removes all the elements from the dictionary
# print(student_info_copy.clear())

print("")
# # Pop -- Removes the element with the specified key
student_info.pop("Name")
print(student_info)

print("")
# Values -- Returns a list containing the dictionary's values
print(student_info.values())
