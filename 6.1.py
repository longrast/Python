def main(x):
    dict41 = {'NIT':0, 'XML':1, 'MUPAD':2}
    dict42 = {'NIT':7, 'XML':8, 'MUPAD':9}
    dict31 = {'MAX':dict41[x[1]], 'XS':3} 
    dict32 = {1995:4, 1987:5}
    dict33 = {1967:6, 1995:dict42[x[1]]}
    dict21 = {1967:dict31[x[3]], 1995:dict32[x[0]]}
    dict22 = {1995:dict33[x[2]], 1987:10}
    dict1 = {2016:dict21[x[2]], 1977:dict22[x[0]]}
    return dict1[x[4]]

if __name__ == "__main__":
    print(main([1995, 'NIT', 1967, 'XS', 1977]))
