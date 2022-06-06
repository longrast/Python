def main(x): #16-ная маска
    e = x & 0x80000000 
    d = x & 0x7ffc0000
    c = x & 0x0003fe00
    b = x & 0x00000100
    a = x & 0x000000ff
    e = e >> 1
    b = b << 23
    d = d >> 18
    c = c << 4
    a = a << 22
    return b+e+a+c+d

def main1(x): #2-ная маска
    a = x & 0b1111_1111
    b = (x >> 10) & 0b1111_1111
    c = (x >> 26) & 0b1111_1111
    d = (x >> 31) & 0b1111_1111
    result = b | (c << 16) | (c << 21) | (c << 31)
    return result 


print(main(0xf450e8ed))
