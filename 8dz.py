def main(x):
    di = {}
    al = []
    sl = []
    a = x.split('|')
    a = a[1::2]
    for i in range(0, len(a)):
        string = a[i]
        string = string.replace(" ", "")
        string = string.replace('\n', '')
        pos1 = string.find('list')
        pos2 = string.find(').')
        al.append(string[0:pos1])
        sl.append(string[pos1+5:pos2].split("'")[1::2])
    di = dict(zip(al, sl))
    return di

print(main("( | zazati list('ononbi' 'biised' 'orso_950' 'rati_568'). | | anqu\nlist( 'maed' 'onen_496''texe_452' ).|)"))
print(main("(| lage list( 'beer' 'inan' 'qucein' ). | |rizaxe list( 'veon_221' 'beisus' 'telaar' ). |)"))
print(main("( | zazati list('ononbi' 'biised' 'orso_950' 'rati_568'). | | anqu\nlist( 'maed' 'onen_496''texe_452' ).|)"))
