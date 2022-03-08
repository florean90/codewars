def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    result = []
    while True:
        if lng > wdth:
            lng -= wdth
            result.append(wdth)
        elif wdth > lng:
            wdth -= lng
            result.append(lng)
        else:
            result.append(lng)
            break
    return result




print(sqInRect(99, 3))