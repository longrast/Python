from math import floor, asin, sin, sqrt

def main(z):
    a = (((floor(27*z))**2) / 84) - asin(z)**4
    b = 32*sin(28*z)**6 - 64*z
    f = sqrt(a) + b
    return f

if __name__ == "__main__":
    print(main(0.75))
