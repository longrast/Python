def main(a, n):
    var = 1
    for c in range(1, n+1):
        temp = 0
        for j in range(1, a+1):
            temp += 58*(((c**2)-26*c)**3)-((j**5)/98)-(c**6)
        var *= temp
    return var

if __name__ == "__main__":
    print(main(7, 4))