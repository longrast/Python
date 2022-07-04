from math import floor

def main(y, z):
    a = 86*((y**2)+6*z+56)**6
    b = 82*(floor((y**2)-72*y-62*(z**3)))**7
    f = z + a - b
    return f

if __name__ == "__main__":
    print(main(0.05, 0.83))

