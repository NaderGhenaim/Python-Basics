# Functions
def greet(first_name, last_name):
    print(f"Hey, {first_name} {last_name}.")

def addition():
    x = input("Enter a number: ")
    y = input("Enter another number: ")
    print(int(x) + int(y))

greet("Nader", "Ghenaim")
addition()

# increments numbers by 1
def increment(number, by = 1):
    return number + by

print(increment(2))
print(increment(2, 5))

# * - allows to push multiple arguments in a function
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multiply(2, 3, 4))

# ** - Unpacking arguments
# function allows multiple keyword arguments to be passed as a dictionary
def save_user(**user):
    print(user)

save_user(id=1, name="Nader", age=19)
