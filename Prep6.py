def main(x):
    dict41 = {1985:4, 2020:5}
    dict42 = {1985:8, 2020:9}
    dict31 = {'SCAML':0, 'OPAL':1, 'MESON':2}
    dict32 = {1957:3, 1980:dict41[x[1]], 1979:6}
    dict33 = {1974:dict42[x[1]], 2017:10}
    dict21 = {1974:dict31[x[2]], 2017:dict32[x[3]]}
    dict22 = {1957:7, 1980:dict33[x[0]], 1979:11}
    dict1 = {1979:dict21[x[0]], 1976:dict22[x[3]]}
    return dict1[x[4]]

if __name__ == "__main__":
    print(main([2017, 1985, 'OPAL', 1979, 1979]))
