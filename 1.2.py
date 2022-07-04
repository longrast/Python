from math import sqrt, pow, ceil

def main(x, y):
    a1 = (34-((y**3)/21)-x)**6
    a = sqrt(37*a1)
    b1 = 66*(x**5)+(ceil((y**3)-(x/87)-(y**2)))**7
    b2 = (91*y - 1 - x**2)**5
    b = b1/b2
    f = a+b
    return f

if __name__ == "__main__":
    print(main(0.57, -0.13))

