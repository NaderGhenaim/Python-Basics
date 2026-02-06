# class Cart:
#     def __init__(self, items=None):
#         self.items = []

#     def add(self, x):
#         self.items.append(x)


# a = Cart()
# b = a
# a.add("pen")
# b.add("pad")
# print(len(a.items), len(b.items))

class Counter:
    def __init__(self):
        self.n = 0


def bump(c):
    c.n += 1
    c = Counter()
    c.n += 5


x = Counter()
bump(x)
print(x.n)
