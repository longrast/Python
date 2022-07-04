from math import atan, cos

def main(z):
    if z < -71:
        y = 98*(0.03-z- z**3)**2 +0.02
    elif -71 <= z < 20:
        a = sin(z+((z**2)/32)+39* z**3)**5
        y = 19* z**2 - a/66 - 7*atan(59* z**2)**6
    elif 20 <= z < 106:
        y = 1+91*cos(z)
    elif 106 <= z < 190:
        y = (z**3 -19)**7 - z**4 - 39* z**3
    elif z >= 190:
        98*(z**3 -15)**6 - 30* z**2 - 82*(z**2 - z**3 -0.03)**3
    return y

if __name__ == "__main__":
    print(main(80))

