import random

def naive_mul(x, y):
    r = x
    for i in range(0, y-1):
        x = x + r
    assert r * y == x, "Что-то пошло не так"
    return r, y, x


for i in range(0,10):
    print(naive_mul(random.randint(1,10), random.randint(1,10)))
