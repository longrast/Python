def main(x):
    alphabet = []
    slowar = []
    a = x.replace(' ', '').replace('\n', '').replace('.do', '').replace('.end', '').split('auto')
    for i in range(1, len(a)):
        temp = a[i].split('->')
        alphabet.append(temp[1])
        slowar.append(int(temp[0]))
    dictionary = dict(zip(alphabet, slowar))
    return dictionary

if __name__ == "__main__":
    print(main('.do auto 2243 -> rea auto 159 -> xear_332 auto 1587 -> tirixe_881 .end'))
