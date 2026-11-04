# Variables and Calling Back Data
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
