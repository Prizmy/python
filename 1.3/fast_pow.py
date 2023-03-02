import random

def fast_pow(x, y):
    summ = x
    for i in range(0, y - 1):
        prevSumm = 0
        for j in range(0, x):
            prevSumm += summ
        summ = prevSumm
    return summ


for i in range(0,20):
    a = random.randint(1,10)
    b = random.randint(1,10)
    assert (fast_pow(a, b) == a**b)
print("Done")
