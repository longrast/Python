def main(x):
    dict31 = {'JSON':0, 'TCSH':1, 'TLA':2}
    dict32 = {'JSON':6, 'TCSH':7, 'TLA':8}
    dict21 = {2002:dict31[x[1]], 2019:3, 1967:4}
    dict22 = {2002: dict32[x[1]], 2019:9, 1967:10}
    dict1 = {2019:dict21[x[0]], 2013:5, 1975:dict22[x[0]]}
    return dict1[x[3]]

if __name__ == "__main__":
    print(main([2002, 'TCSH', 'COBOL', 1975]))
