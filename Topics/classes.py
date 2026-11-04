# Classes: blueprint for creating new objects
# Objects: instance of a class
# Class: Human
# Object: Nader, Gautami = Human()
class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

    def __eq__(self, other):
        return self.x == another.x and self.y == another.y

    def __gt__(self, other):
        return self.x > another.x and self.y > another.y

    def __lt__(self, other):
        return self.x < another.x and self.y < another.y

    def __add__(self, other):
        return Point(self.x + another.x, self.y + another.y)

    def __mul__(self, other):
        return Point(self.x * another.x, self.y * another.y)


point = Point(1, 2)
print(point.default_color)
point.draw()

Point.default_color = "brown"
another = Point(3, 4)
print(another.default_color)
another.draw()

point = Point.zero()
print(point)

point = Point(2, 3)
combine = point + another
print(combine.x)
print(point > another)
print(point + another)
print(point * another)

# Containers
class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)

cloud = TagCloud()
cloud["Python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)

# Properties
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

product = Product(-15)

# Inheritance allows to define common functions
# Animal is base and mammal anf fish is the sub
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def walk(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)

class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

#looks at class from first to last
class FlyingFish(Flyer, Swimmer):
    pass

class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is open")
        self.opened = True

    def closed(self):
        if not self.opened:
            raise InvalidOperationError("Stream is closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")
