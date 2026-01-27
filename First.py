# Variables and Calling Back Data
'''
students_count = 1000
rating = 4.99
is_published = False
course_name = "Computer programming"
Average = students_count / rating

# Multiplies rating by 3 and prints answer
print(rating * 3)

# prints H 3 times
print("H" * 3)

# how many characters in course_name
print(len(course_name))
print(course_name[0:9])

full = f"{Average} {course_name} {students_count} {500+students_count}"
print(full)
print(course_name.lower())
print(course_name.upper())
print(course_name.title())
print(course_name.find("gra"))
print("am" in course_name)
print("Cool" not in course_name)

#converting string to int
x = input("x: ")
int(x)
y = int(x) + 1
print(f"x: {x}, y: {y}")

#where something is located in word
fruit = "Apple"
print(fruit[1:-1])

#boolean expressions
print(bool(10 > 4))
print(bool("bag" == "BAG"))

# if else statements
temperature = 70
if (temperature > 80):
    message = "It's frickin hot. "
elif (temperature < 60):
    message = "It's chilly. "
else:
    message = "Pretty good weather today. "
print(message + "Dress appropriately.")

# Logical operators
money = True
fine_shyt = False
employed = False

if money and fine_shyt:
    print("Let em in")
else:
    print("Who is chud")

if (money or fine_shyt) and employed:
    print("Let's get some food")
else:
    print("Get da hell outta here")

age = 22
if 18 <= age < 65:
    print("You gotta work")

# for loops and break
for number in range(3):
    print("Send da nudes. " + "Please. " * (number + 1))

for number in range(1, 4):
    print("No. " * number)

for number in range(2, 10, 2):
    print("Breh. " * number)

success = False
for number in range(3):
    print("Attempt")
    if success:
        print("Success")
        break
    else:
        print("Error")

for x in range(4):
    for y in range(2):
        print(f"({x}, {y})")

for x in "Python":
    print(x)

for x in [4, 7, 3, 11]:
    print(x)

# while loops
number = 100
while number > 0:
    print(number)
    number //= 2

gallons = 5
while True:
    if gallons > 0:
        print("We good")
        gallons -= 1
    else:
        print("Gotta get gas")
        break

command = ""
while command.lower() != "quit":
    command = input(">")
    print("User inpute\ =", command)

list = range(1, 10)
n = 0
count = 0
while True:
    if list[n] % 2 == 0:
        print(list[n])
        count += 1
    n += 1
    if n == list[-1]:
        print("We have", count, "even numbers")
        break

# Functions
def greet(first_name, last_name):
    print(f"Hey, {first_name} {last_name}.")

def addition():
    x = input("Enter a number: ")
    y = input("Enter another number: ")
    print(int(x) + int(y))

greet("Nader", "Ghenaim")
addition()

def increment(number, by = 1):
    return number + by

print(increment(2))
print(increment(2, 5))

def multiply(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multiply([2, 3, 4]))
'''
