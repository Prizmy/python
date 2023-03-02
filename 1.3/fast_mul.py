import random

def fast_mul(x, y):
    bitSumm = 0
    summ = 0
    for i in range(0, y.bit_length()):
        for j in range(0, x.bit_length()):
            bitSumm = bitSumm + (((y >> i & 1) & (x >> j & 1)) << (j + i))
        summ += bitSumm
        bitSumm = 0
    assert x * y == summ, "Что-то пошло не так"
    return x, y, summ


for i in range(0,10):
    print(fast_mul(random.randint(1,10), random.randint(1,10)))
