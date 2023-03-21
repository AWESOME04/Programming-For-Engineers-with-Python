# Python string and methods

# When to use single or double quotation marks

# Indexing: Python indexing starts from 0
UG = "Ghana's 'premier' university"
school = "university"
print("")

# len function
print(len(UG))
print("")

# STRING METHODS

# Capitalize -- Converts the first character to uppercase
print(UG.capitalize())
print(school.capitalize())
print("")

# Count -- Returns the number of times a specified character occurs in a string
print(UG.count("a"))
print("")

# Find -- Searches the string for a specified value and returns the position (index) of where it was found
print(UG.find("a")) # Gives a negative 1 when string isn't found
print("")

# Replace -- Replaces a specified value with another
print(UG.replace("a", "o")) # If what you want to replace is not found then the original string is printed out
print("")

# Index -- Searches the string for a specified value and returns the position of where it was found
print(UG.index("a"))
print("")

# Lower -- Converts a string into lower case
print(UG.lower())
print(school.lower())
print("")

# Upper -- Converts a string into upper case
print(UG.upper())
print(school.upper())
print("")

# Isalnum -- Returns True if all characters in the string are alphanumeric
print(school.isalnum())
print(UG.isalnum()) # Prints false for whitespace and symbols
print("")

# Isdigit -- Returns True if all characters in the string are digits
print(school.isdigit())
print(UG.isdigit())
print("")

# Isspace -- Returns True if all characters in the string are whitespaces
print(school.isspace())
print(UG.isspace())
print("")

# Slipt -- Splits the string at the specified separator, and returns a list
print(school.split())
print(UG.split())
print(len(UG.split()))
print("")

# Startwith -- Returns true if the string starts with the specified value
print(school.startswith("u"))
print(UG.startswith("t"))
print("")

# Endwith -- Returns true if the string ends with the specified value
print(school.endswith("u"))
print(UG.endswith("t"))
print("")

print("Ghana's 'premier' university" )


# ALT
print('Ghana\'s "premier" university' )

country = "Ghana's"
status = '"premier"'


print(school.title())
print(len(school))
print(f"{country} {status} {school}")













