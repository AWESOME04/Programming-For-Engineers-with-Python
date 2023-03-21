# Python list is a collection which is ordered and mutable.
# It allows duplicate members
countries = ["Ghana", "Togo", "Nigeria", "USA", "Ghana"]

# len fucntion
print(len(countries))

# LIST METHODS
# Append -- Adds an element at the end of the list
countries.append("Brazil")
print(countries)

# Clear -- Removes all the elements from the list
# countries.clear()
# print(countries)

# Copy -- Returns a copy of the list
new_countries = countries.copy()
print(new_countries)

# Count -- Returns the number of elements with the specified value
print(countries.count("Ghana"))

# Index -- Returns the index of the first element with the specified value
print(countries.index("Ghana"))

# Sort -- Sorts the list
countries.sort()
print(countries)

countries.sort(reverse=True)
print(countries)


# Reverse -- Reverses the order of the list
countries.reverse()
print(countries)

# Remove -- Removes the first item with the specified value
countries.remove("Ghana")
print(countries)

# Pop -- Removes the element at the specified position
# Not specifying the element removes the last item/ element
countries.pop(2)
print(countries)
