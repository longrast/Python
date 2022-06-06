def main(x):
    match x[0]:
        case ???:
            match x[3]:
                case "???":
                    match x[2]:
                        case ???:
                            return 4
                        case ???:
                            return 3
                        case ???:
                            match x[1]:
                                case "???":
                                    return 0
                                case "???":
                                    return 1
                                case "???":
                                    return 2
                case "???":
                    match x[4]:
                        case "???":
                            return 8
                        case "???":
                            return 9
                        case "???":
                            match x[1]:
                                case "???":
                                    return 5
                                case "???":
                                    return 6
                                case "???":
                                    return 7
        case ???:
            return 10
            

print(main([2008, 'KIT', 1975, 'NINJA', 'FISH']))
#очень примерный шаблон
