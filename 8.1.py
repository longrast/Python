#19
def main(x):
    di = {}
    al = []
    sl = []
    a = x.split('>>')
    a = a[:-1]
    for i in range(0, len(a)):
        string = a[i]
        string = string.replace('(',' ').replace(')',' ')
        string = string.replace('\n', ' ')
        pos2 = string.find('list')
        pos3 = string.find(').')
        sl.append(string[pos2+4:pos3].split(" ")[1:-1])
        string = string.replace(' ', '')
        pos1 = string.find('let')+3
        pos2 = string.find('list')
        al.append(string[pos1:pos2-2])
        sl = de(sl)
    di = dict(zip(al, sl))
    return di


def de(x):
    for i in range(0, len(x)):
        x1 = []
        for j in range(0, len(x[i])):
            if x[i][j] != '':
                x1.append(x[i][j])
        x[i] = x1
    return x

print(main("<section> <<let laso_688 <- list( cexe cea atge erre ).>><< let enge\n<- list( betien beor esti_347 ain_298 ). >> </section>"))
print(main("<section> << let lama <- list(laat_340 aza). >> <<let sodied <- list(\narbe_792 enqu inle_863 gela ). >> << let belees <- list( zain_921 gete\nqule_748 mausbe ). >> </section>"))
