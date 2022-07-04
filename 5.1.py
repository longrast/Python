from math import ceil, log10


def main(x):
    n = len(x)
    y = 0
    for i in range(1, n+1):
        y += 56 * log10(0.01 + 6 * x[ceil(i/4) - 1]) ** 3
    return y

if __name__ == "__main__":
    print(main([0.35, 0.62]))
