#36
def main(x):
    e = x & 0xc0000000
    d = x & 0x3fff8000
    c = x & 0x00007ff0
    b = x & 0x00000008
    a = x & 0x00000007
    a = a << 3
    b = b >> 3
    c = c << 2
    d = d << 2
    e = e >> 29
    return a+b+c+d+e

if __name__ == "__main__":
    print(main(0x3f19ad00))

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
