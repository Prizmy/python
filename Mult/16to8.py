def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y

def mul16(x, y):
    a = x >> 8
    b = x
    c = y >> 8
    d = y
    a_c = mul_bits(a, c, 8)
    b_c = mul_bits(b, c, 8)
    a_d = mul_bits(a, d, 8)
    b_d = mul_bits(b, d, 8)
    return b_d + ((a_d + b_c) << 8) + (a_c << 16)

print(mul16(153, 2913))
print(153 * 2913)
