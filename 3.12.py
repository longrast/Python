from math import pow, cos


def main(b, m, n):
    sum = 1
    for i in range(1, n+1):
        var = 0
        for k in range(1, m+1):
            for j in range(1, b+1):
                var += (cos(80 * pow(i, 2) + 78 * j + pow(k, 3)) - pow(j, 7) - 1)
        sum *= var
    return sum

if __name__ == "__main__":
    print(main(4, 7, 2))
