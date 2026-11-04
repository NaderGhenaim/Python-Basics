# Lists
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 3
combine = letters + zeros
print(combine)

number = list(range(20))
print(number)
print(number[::2])

chars = list("Nader")
print(chars)

numbers = [1, 2, 3, 4, 5]
first, *other, last = numbers
print(first)
print(last)
print(other)

for index, letter in enumerate(letters):
    print(index, letter)

# append inserts at end of list
letters.append("d")
letters.insert(0, "|")
print(letters)

# pop removes last item in list
letters.pop()
letters.remove("b")
del letters[0]
print(letters)

if "d" in letters:
    print(letters.index("d"))
print(letters.count("a"))

# sorting
numbers = [3, 51, 2, 8, 7]
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))

# lambda function to sort
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# lambda = paramater: expression, item: item[1] means sort by second item in tuple
items.sort(key=lambda item: item[1])
print(items)

# map creates new list based on function and index provided
prices = list(map(lambda item: item[1], items))
#list comprehension way of doing same thing
prices = [item[1] for item in items]
print(prices)

filtered = list(filter(lambda item: item[1] >= 10, items))
#list comprehension way of doing same thing
filtered = [item for item in items if item[1] >= 10]
print(filtered)

# zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# zip combines multiple lists into tuples
print(list(zip("abc", list1, list2)))

# stack data structure
# pops last item in list and returns to new last
browsing_history = []
browsing_history.append("google.com")
browsing_history.append("youtube.com")
browsing_history.append("gmail.com")
print(browsing_history)
last_visited = browsing_history.pop()
print("Last visited:", last_visited)
print(browsing_history)
print("Redirecting to", browsing_history[-1])
last_visited = browsing_history.pop()
print("Redirecting to", browsing_history[-1])
last_visited = browsing_history.pop()
if not browsing_history:
    print("No pages in history")

# Queues
# like a queue in real life, first in first out
from collections import deque
queue = deque([])
queue.append("A")
queue.append("B")
queue.append("C")
queue.popleft()
print(queue)
if not queue:
    print("Queue is empty")

# tuples are a read only list, can't change values
point = (10, 20) + (30, 40)
print(point[3])

# swapping variables
x = 10
y = 11

# x, y = 11, 10
x, y = y, x
print(x, y)

# Arrays, optimizes space for large lists of numbers
# only for performance problems, same as lists and tuples
# can use array.shape from external libraries to find shape of arrays 
from array import array

array("i", [1, 2, 3])

# sets
first = set([1, 2, 3, 1, 2])
second = {3, 4, 5}

print(first | second)  # union
print(first & second)  # intersection
print(first - second)  # difference
print(first ^ second)  # unique to each set

# dictionary
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
print(point["x"])
print(point.get("a", 0))
del point["y"]
print(point)
for key in point:
    print(key, point[key])

# generators
from sys import getsizeof
values = (x * 2 for x in range(1000))
print("Generator:", getsizeof(values))

values = [x * 2 for x in range(1000)]
print("List:", getsizeof(values))

# Unpacking operator
stuff = [1, 2, 3]
print(stuff)
print(*stuff)

values = [*range(5), *"Hello"]
print(values)

first = {"x": 1}
second = {"y": 2}
combined = {**first, **second, "z": 3}
print(combined)


# Excersise
sentence = "This is a common interview question"

def most_frequent(sentence):
    frequency = {}
    for char in sentence:
        if char in frequency:
            frequency[char.lower()] += 1
        else:
            frequency[char.lower()] = 1
    most_common = sorted(frequency.items(), key=lambda kv: kv[1], reverse=True)
    return most_common[0]

print(most_frequent(sentence))
