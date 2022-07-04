from math import pow, log, exp 


def main(x):
    a = 75 * exp(pow(x, 3)) - pow(log(x, 2), 5)
    b = 77 * x ** 5 - (x - 35 * x ** 2 - (x ** 3) / 86) ** 7
    c = 44 * x ** 7 + (x - 34 - 74 * x ** 2) ** 3
    d = x ** 4 / 80
    y = a / b + c / d
    return y

if __name__ == "__main__":
    print(main(0.22))

