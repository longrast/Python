from math import acos, ceil

def main(x, y):
    n = len(x)
    temp = 0
    for i in range(1, n+1):
        temp += 64* acos(14*((y[ceil((i/4)-1)])**2) -45* (x[n-ceil(i/4)])**3)
    f = 83*temp
    return f

if __name__ == "__main__":
    print(main([-0.04, 0.2], [-0.13, -0.15]))