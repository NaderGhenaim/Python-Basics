class Cart:
    def __init__(self, items=None):
        self.items = []

    def add(self, x):
        self.items.append(x)


a = Cart()
b = a
a.add("pen")
b.add("pad")
print(len(a.items), len(b.items))
