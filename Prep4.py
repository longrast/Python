def main(n):
    if n == 0:
        return 0.00
    elif n >= 1:
        return ((60*(main(n-1)**3) - 76 - 22*(main(n-1)**2))/89) + 1
    else:
        print("BAD")

if __name__ == "__main__":
    print(main(8))
