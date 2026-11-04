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

#* allows to push multiple arguments in a function
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multiply(2, 3, 4))

# ** Unpacking arguments
def save_user(**user):
    print(user)

save_user(id=1, name="Nader", age=19)

#Practice Exercise: FizzBuzz
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(1))
