def main(z):
    n = len(z)
    f = 0
    for i in range(1, n+1):
        f += (12* (z[n-i])**2 - (z[n-i])**3)**3
    return f

if __name__ == "__main__":
    print(main([-0.13, -0.04, -0.69, -0.38, 0.58, 0.76, 0.55, 0.91]))
