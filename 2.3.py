from math import log2, cos

def main(y):
    if y < 170:
        f = y**4
    elif 170 <= y < 219:
        f = 60* log2(y+ y**2 +84) - 57* cos(y)**4 - 7* y**6
    elif y >= 219:
        f = (y**3 - 4*y - y**2)**4 - y**15 - 26*(round(y**3 - (y/61) - 25* y**2))**7
    return f

if __name__ == "__main__":
    print(main(75))

