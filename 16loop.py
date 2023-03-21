# Loop
# A loop is used for iterating over a sequence

# For loop

# While loop

# Assignment
# Mark up Language
# A markup language is a computer language that consists of easily understood keywords, names, or tags that help format the overall view of a page and the data it contains.
# A markup language is a computer language that is used to annotate text or other data with instructions that describe how the text or data should be displayed or otherwise processed. Markup languages are used to format and structure text, and to provide additional information about the content being marked up.
# The most commonly used markup language is HTML (Hypertext Markup Language), which is used to create web pages. HTML is used to describe the structure and formatting of a web page, including the text, images, links, and other elements that make up the page. Other examples of markup languages include XML (Extensible Markup Language), which is used for data exchange between applications, and Markdown, which is a simple markup language used for formatting text documents.
# Markup languages use tags or codes that are embedded in the text to indicate how the text should be formatted. For example, in HTML, the <p> tag is used to indicate the start of a paragraph, and the </p> tag is used to indicate the end of a paragraph. Markup languages are typically human-readable, which means that the markup codes can be easily understood by people who are familiar with the language.


# 3 examples of mark up languages
# Some examples of a markup language are BBC, HTML, SGML, and XML.

# HTML (Hypertext Markup Language) - used to create web pages by marking up text, images, links, and other elements on the page.

# XML (Extensible Markup Language) - used for data exchange between applications by marking up data elements and describing their relationships.

# Markdown - used for formatting text documents by marking up headings, lists, links, and other elements.

# My Document This is some text in my document. - Item 1 - Item 2 [Link to Google](https://www.google.com/)

# Are mark up languages programming languages?. Explain your answer.
# A markup language is not a programming language. It is special markings, interspersed with plain text, which, if removed or ignored, leave the plain text as a complete whole.
# Or, those markings can be interpreted in a predefined manner (make this text bold, make this text an ordered list) that enhances its presentation to the reader.
# In contrast, plain text may be (and often is) part of a computer program; however, its representation varies according to the programming language and the programmer's writing style.
# Importantly, if all non-plain-text components of a computer program are removed, the remaining plain text is not guaranteed to be complete or correctly ordered.

# Loop through List
fruits = ["Mango", "Banana", "Apple", "Orange", "Strawberry"]

for fruit in enumerate(fruits):
    print(fruit)

for fruit in enumerate(fruits):
    if fruit[1] == "Mango":
        print(fruit)

# Loop through multiple Lists simultaneously using zip method
    if fruit == "Apple":
        break
names = ["Ken", "Ama", "Kwame"]
scores = [67, 99, 100]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# The Range Method
for x in range(5, 10, 2):
    print(x)

# range method and loops
# range(start, stop-1, step)
for x in range(5, 11):
    print(x)

# Voting years in Ghana using range methods
for x in range(1992, 2023, 4):
    print(f"{x} was a voting year")


# Loop through Dictionary


# Exercise
# 1. Find all the even numbers in a range of 0 - 50
for i in range(0, 52):
    if i % 2 == 0:
        print(i)

print("")
print("")

# 2. Find the sum of all elements in a list
num_list = [1, 2, 3, 4, 5, 6, 7]

tot = 0
for num in num_list:
    tot += num
print(tot)

# 3. Find the factorial of a number
num = int(input("Enter the number:"))

factorial = 1
if num < 0:
    print("Sorry, factorial for negative numbers do not exist. Try a positive number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial} ")


# WHILE LOOPS
while x < 20:
    print(x)
    x += 1

limit = 3
count = 0

while count < limit:
    data = input("Enter your data:")
    print(f"iteration count: {count}")
    count += 1

while count < limit:
    data = input("Enter your number: ")
    if data.isnumeric():
        print(f"{data} is numeric")
        break
    else:
        if count < 1:
            print("Wrong Input\nEnter a numeric value")
        elif count == 1:
            print("Last Try")
    count += 1

