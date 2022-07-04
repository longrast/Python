from math import log10

def main(y):
    if y < -53:
        f = 15*y
    elif -53 <= y < 41:
        f = y**6 - 0.02
    elif 41 <= y < 59:
        f = log10(0.06+ y**3)**7 + 82*(53*y)**6
    elif 59 <= y < 116:
        f = (27 + 60* y**3 + y/90)**2 -1
    else:
        f = 26* y**4
    return f

if __name__ == "__main__":
    print(main(59))