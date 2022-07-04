from math import pow, tan, atan

def main(z):
    if z < -23:
        y = pow(z, 3) / 71
    elif -23 <= z <= 42:
        y = 18 * pow(z, 5)
    elif 42 <= z <= 63:
        y = 3 * pow(z, 2) + 35 * pow(tan(z), 5)
    elif 63 <= z <= 100:
        a = z / 82
        b = pow(z, 3) / 40
        c = 99 * pow(z, 2)
        d = pow(z, 8)
        y = pow((a - b - c), 7) + pow(z, 8)
    elif z >= 100:
        a = 9 * pow(atan(z), 7)
        b = 11 * pow((3 * pow(z, 2) + 88 + z), 2)
        y = a + b + 57
    return y

if __name__ == "__main__":
    print(main(18))

