import random

def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul_16_3(x, y):
    x1, x2 = x >> 8, x & 255
    y1, y2 = y >> 8, y & 255
    n, n1 = 16, 8
    mul1 = mul_bits(x1, y1, n1)
    mul2 = mul_bits(x2, y2, n1)
    mul3 = mul_bits(x1 + x2, y1 + y2, n)
    return (mul1 << n) - (mul1 << n1) + mul2 - (mul2 << n1) + (mul3 << n1)


for i in range(0, 50):
    for j in range(0, 50):
        a = random.randint(100, 10000)
        b = random.randint(100, 10000)
        assert (mul_16_3(a, b) == a * b)
