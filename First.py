# # Variables and Calling Back Data
# students_count = 1000
# rating = 4.99
# is_published = False
# course_name = "Computer programming"
# Average = students_count / rating

# # Multiplies rating by 3 and prints answer
# print(rating * 3)

# # prints H 3 times
# print("H" * 3)

# # how many characters in course_name
# print(len(course_name))
# print(course_name[0:9])

# full = f"{Average} {course_name} {students_count} {500+students_count}"
# print(full)
# print(course_name.lower())
# print(course_name.upper())
# print(course_name.title())
# print(course_name.find("gra"))
# print("am" in course_name)
# print("Cool" not in course_name)

# #converting string to int
# x = input("x: ")
# int(x)
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# #where something is located in word
# fruit = "Apple"
# print(fruit[1:-1])

# #boolean expressions
# print(bool(10 > 4))
# print(bool("bag" == "BAG"))

# # if else statements
# temperature = 70
# if (temperature > 80):
#     message = "It's frickin hot. "
# elif (temperature < 60):
#     message = "It's chilly. "
# else:
#     message = "Pretty good weather today. "
# print(message + "Dress appropriately.")

# # Logical operators
# money = True
# fine_shyt = False
# employed = False

# if money and fine_shyt:
#     print("Let em in")
# else:
#     print("Who is chud")

# if (money or fine_shyt) and employed:
#     print("Let's get some food")
# else:
#     print("Get da hell outta here")

# age = 22
# if 18 <= age < 65:
#     print("You gotta work")

# # for loops and break
# for number in range(3):
#     print("Send da nudes. " + "Please. " * (number + 1))

# for number in range(1, 4):
#     print("No. " * number)

# for number in range(2, 10, 2):
#     print("Breh. " * number)

# success = False
# for number in range(3):
#     print("Attempt")
#     if success:
#         print("Success")
#         break
#     else:
#         print("Error")

# for x in range(4):
#     for y in range(2):
#         print(f"({x}, {y})")

# for x in "Python":
#     print(x)

# for x in [4, 7, 3, 11]:
#     print(x)

# # while loops
# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# gallons = 5
# while True:
#     if gallons > 0:
#         print("We good")
#         gallons -= 1
#     else:
#         print("Gotta get gas")
#         break

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("User inpute\ =", command)

# list = range(1, 10)
# n = 0
# count = 0
# while True:
#     if list[n] % 2 == 0:
#         print(list[n])
#         count += 1
#     n += 1
#     if n == list[-1]:
#         print("We have", count, "even numbers")
#         break

# # Functions
# def greet(first_name, last_name):
#     print(f"Hey, {first_name} {last_name}.")

# def addition():
#     x = input("Enter a number: ")
#     y = input("Enter another number: ")
#     print(int(x) + int(y))

# greet("Nader", "Ghenaim")
# addition()

# def increment(number, by = 1):
#     return number + by

# print(increment(2))
# print(increment(2, 5))

# #* allows to push multiple arguments in a function
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
# print(multiply(2, 3, 4))

# # ** Unpacking arguments
# def save_user(**user):
#     print(user)

# save_user(id=1, name="Nader", age=19)

# #Practice Exercise: FizzBuzz
# def fizz_buzz(input):
#     if input % 3 == 0 and input % 5 == 0:
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     return input

# print(fizz_buzz(3))
# print(fizz_buzz(5))
# print(fizz_buzz(15))
# print(fizz_buzz(1))

# # Lists
# letters = ["a", "b", "c"]
# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 3
# combine = letters + zeros
# print(combine)

# number = list(range(20))
# print(number)
# print(number[::2])

# chars = list("Nader")
# print(chars)

# numbers = [1, 2, 3, 4, 5]
# first, *other, last = numbers
# print(first)
# print(last)
# print(other)

# for index, letter in enumerate(letters):
#     print(index, letter)

# # append inserts at end of list
# letters.append("d")
# letters.insert(0, "|")
# print(letters)

# # pop removes last item in list
# letters.pop()
# letters.remove("b")
# del letters[0]
# print(letters)

# if "d" in letters:
#     print(letters.index("d"))
# print(letters.count("a"))

# # sorting
# numbers = [3, 51, 2, 8, 7]
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(sorted(numbers, reverse=True))

# # lambda function to sort
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]

# # lambda = paramater: expression, item: item[1] means sort by second item in tuple
# items.sort(key=lambda item: item[1])
# print(items)

# # map creates new list based on function and index provided
# prices = list(map(lambda item: item[1], items))
# #list comprehension way of doing same thing
# prices = [item[1] for item in items]
# print(prices)

# filtered = list(filter(lambda item: item[1] >= 10, items))
# #list comprehension way of doing same thing
# filtered = [item for item in items if item[1] >= 10]
# print(filtered)

# # zip function
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# # zip combines multiple lists into tuples
# print(list(zip("abc", list1, list2)))

# # stack data structure
# # pops last item in list and returns to new last
# browsing_history = []
# browsing_history.append("google.com")
# browsing_history.append("youtube.com")
# browsing_history.append("gmail.com")
# print(browsing_history)
# last_visited = browsing_history.pop()
# print("Last visited:", last_visited)
# print(browsing_history)
# print("Redirecting to", browsing_history[-1])
# last_visited = browsing_history.pop()
# print("Redirecting to", browsing_history[-1])
# last_visited = browsing_history.pop()
# if not browsing_history:
#     print("No pages in history")

# # Queues
# # like a queue in real life, first in first out
# from collections import deque
# queue = deque([])
# queue.append("A")
# queue.append("B")
# queue.append("C")
# queue.popleft()
# print(queue)
# if not queue:
#     print("Queue is empty")

# # tuples are a read only list, can't change values
# point = (10, 20) + (30, 40)
# print(point[3])

# # swapping variables
# x = 10
# y = 11

# # x, y = 11, 10
# x, y = y, x
# print(x, y)

# # Arrays, optimizes space for large lists of numbers
# # only for performance problems, same as lists and tuples
# from array import array

# array("i", [1, 2, 3])

# # sets
# first = set([1, 2, 3, 1, 2])
# second = {3, 4, 5}

# print(first | second)  # union
# print(first & second)  # intersection
# print(first - second)  # difference
# print(first ^ second)  # unique to each set

# # dictionary
# point = dict(x=1, y=2)
# point["x"] = 10
# point["z"] = 20
# print(point["x"])
# print(point.get("a", 0))
# del point["y"]
# print(point)
# for key in point:
#     print(key, point[key])

# # generators
# from sys import getsizeof
# values = (x * 2 for x in range(1000))
# print("Generator:", getsizeof(values))

# values = [x * 2 for x in range(1000)]
# print("List:", getsizeof(values))

# # Unpacking operator
# stuff = [1, 2, 3]
# print(stuff)
# print(*stuff)

# values = [*range(5), *"Hello"]
# print(values)

# first = {"x": 1}
# second = {"y": 2}
# combined = {**first, **second, "z": 3}
# print(combined)


# # Excersise
# sentence = "This is a common interview question"

# def most_frequent(sentence):
#     frequency = {}
#     for char in sentence:
#         if char in frequency:
#             frequency[char.lower()] += 1
#         else:
#             frequency[char.lower()] = 1
#     most_common = sorted(frequency.items(), key=lambda kv: kv[1], reverse=True)
#     return most_common[0]

# print(most_frequent(sentence))
