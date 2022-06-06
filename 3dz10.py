from math import tan, floor, ceil


def main(m, b, n, p):
    f = 0
    f1 = 0
    f2 = 0
    for j in range(1, n+1):
        for k in range(1, b+1):
            for c in range(1, m+1):
                f+=(28*ceil(k-c**3-j**2)**2-96*p**4-(c**6/27))

            f1*=f

        f2+=f1



    return f

print(main(4, 5, 4, 0.25))
print(main(6, 4, 5, 0.22))
