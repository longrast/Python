from math import sin

def main(a, x, n):
    sum1 = 0
    sum2 = 0
    for i in range(1, a+1):
        sum1 += (74* i**2 +93*x+79)**4 + i**5 + sin(i)**2
    for k in range(1, a+1):
        for i in range(1, n+1):
            sum2 += ((k/82 - (i**3)/40 - 99* k**2)**7 + x**8)
    f = sum1 - sum2
    return f

if __name__ == "__main__":
    print(main(6, -0.68, 3))