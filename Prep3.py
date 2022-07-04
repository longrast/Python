def main(m, x, n, a):
    sum1 = 0
    for i in range(1, m+1):
        sum1 += x**7 - 1 - 9*i
    sum2 = 0
    for j in range(1, a+1):
        for c in range(1, n+1):
            sum2 += 32* j**3 + 21* c**2 - 80
    f = sum1 + sum2
    return f

if __name__ == "__main__":
    print(main(3, -0.53, 8, 3))
