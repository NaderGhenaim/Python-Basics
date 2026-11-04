# Exceptions
try:
    with open("First.py") as file:
        print("File opened.")
        file.__
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("You are", age, "years old.")

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or negative.")
    return 10 / age
try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
