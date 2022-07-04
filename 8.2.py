def main(x):
    a = x.replace(" ", "").replace('\n', '').split("end,begin")
    alphabet = []
    slowar = []
    for i in range(0, len(a)):
        string = a[i]
        posFirstLetter1Word = string.find('>') + 2
        f1 = string.find('(')
        f2 = string.find(')')
        qwerty = string[f1+1:f2:]
        qwerty = qwerty.split(';')
        for k in range(0, len(qwerty)):
            qwerty[k] = int(qwerty[k][1:])
        slowar.append(string[posFirstLetter1Word:-1:])
        alphabet.append(qwerty)
    dictionary = dict(zip(slowar, alphabet))
    return dictionary

print(main('begin begin #(#895 ; #-7069 ;#-5587 ) |> "xeve" end, begin #( #-4131\n; #8772 ) |> "vece" end,begin #( #-1520 ; #434 ; #-9003 ) |>\n"onatbe_35"end,begin#(#-2874 ; #6432 ;#5365; #9906 )|>"qued" end, end'))
