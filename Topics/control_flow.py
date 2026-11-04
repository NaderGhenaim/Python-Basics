# boolean expressions
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
