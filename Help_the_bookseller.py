import string

def stock_list(listOfArt, listOfCat):
    if listOfArt == [] or listOfCat == []:
        return ""
    artDict = {i: 0 for i in string.ascii_uppercase}
    for i in listOfArt:
        artDict[i[0]] += int(i.split()[1])
    return " - ".join(f"({i} : {artDict[i]})" for i in listOfCat)

















b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c))