# Python set is a collection which is unordered and not mutable.
# It does not allow duplicate members

# An empty set is a dictionary
fruits = {}

print(fruits)
print(type(fruits))

fruit = {"Mango", "Banana", "Apple", "Berry"}
print(fruit)
print(type(fruit))

# Type Casting
Veggies = ["Tomato", "Eggplant", "Cabbage"]
print(Veggies)
Veggies_set = set(Veggies)
print(Veggies_set)


# Union and Intersection
first_score = {30, 40, 50}
second_score = {20, 70, 80}

print(first_score.intersection(second_score))
print(first_score & second_score)  # ALT

print(first_score.union(second_score))
print(first_score | second_score)  # ALT

# Difference
print(first_score.difference(second_score))


# Add
first_score.add(90)
print(first_score)
