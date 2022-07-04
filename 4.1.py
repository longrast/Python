from math import sin

def main(n):
    if n == 0:
        return -0.41
    elif n == 1:
        return -0.33
    elif n >= 2:
        return (sin(80*(main(n-2)**3)-(main(n-1))-44)**3)-((main(n-2))+(main(n-1)**2)+1)

if __name__ == "__main__":
    print(main(9))
