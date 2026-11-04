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
