def main(x):
    e = x & 0x80000000
    d = x & 0x7fff0000
    c = x & 0x0000ff80
    b = x & 0x00000040
    a = x & 0x0000003f
    a << 25
    b << 18
    c << 8
    d >> 16
    return a+b+c+d+e

if __name__ == "__main__":
    print(main(0x663d60fe))

'''
0001 1
0010 2
0011 3
0100 4
0101 5
0110 6
0111 7
1000 8
1001 9
1010 A
1011 B
1100 C
1101 D
1110 E
1111 F
'''
