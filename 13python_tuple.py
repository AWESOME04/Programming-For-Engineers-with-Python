# Python tuple is a collection which is ordered.
# A tuple is not mutable
# It allows duplicate members
fruits = ('Banana', 'Mango', 'Apple', 'Banana')
print(fruits[-1])

# Has only two methods - Index and Count
fruits.count("Banana")
print(fruits)

fruits.index("Apple")
print(fruits)

# Unpack Tuple
x, *y = (2, 0, 9)

print(x)
print(y)







