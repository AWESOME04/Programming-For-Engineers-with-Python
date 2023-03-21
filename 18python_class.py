# A class is a blue-print for creating objects.
# The object becomes an instance of the class.

# The object then becomes an instance of the class
# OOP is a programming paradigm in which the code used to implement programming logic is
# based on the concepts of "objects"

# Procedural Programming is about writing procedures or functions that perform operations on the data.

# Programming paradigm is basically the methodology in which programming is done

# Synonyms to orient:
# Align, Place, Position, Situate

# Conclusion:
# OOP:
# * Provides a clear structure for our program
# * Makes it possible to create full reusable applications with less code and shorter development time
# * Helps to keep the Python code DRY "Don't Repeat Yourself"

school = "University of Ghana"

class BakingPan:
    unit_price = 5

    def __init__(self, flour , sugar, special_ingredient):
        self.flour = flour
        self.sugar = sugar
        self.special_ingredient = special_ingredient

    def bread_name(self):
        return f"{self.unit_price} and {self.special_ingredient} bread \n"


    def total_price(self, quantity):
        total = quantity * self.unit_price
        return f"The total price of {quantity} {self.bread_name()} = GHC {total}"

    # def myFunc():
    #     print("This is my baking pan function")


# print(BakingPan.myFunc())

bread1 = BakingPan("Soft", 20, "Wheat")
bread2 = BakingPan("Hard", 10, "Banana")

print(bread1.bread_name())
print(bread1.sugar)
print(bread2.special_ingredient)
print(bread2.total_price(3))

# Flour, Sugar, Special_Ingredient
# bread1.flour = "Soft"
# bread1.sugar = 20
# bread1.special_ingredient = "Wheat"

# bread2 = BakingPan()
# bread2.flour = "Hard"
# bread2.sugar = 10
# bread2.special_ingredient = "Coconut"
#


# Special methods - init method











