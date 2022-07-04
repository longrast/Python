from math import ceil

def main(y, z):
    n = len(y)
    sum = 0
    for i in range(1, n+1):
        sum += 53*(86+ (y[ceil((i/4)-1)])**2 +((z[n-ceil(i/4)])**3)/81)**3
    return sum

if __name__ == "__main__":
    print(main([0.69, 0.94, 0.85], [0.93, -0.5, 0.05]))

