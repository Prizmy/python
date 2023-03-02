def mul_by_15(x):
    x1 = x + x
    x2 = x1 + x1
    x3 = x2 + x2
    return x3 - (x - x3)


print(mul_by_15(1))
print(mul_by_15(2))
