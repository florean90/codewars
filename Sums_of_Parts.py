# def parts_sums(ls):
#     return [sum(ls[i:]) for i in range(len(ls)+1)]

# parts_sums = lambda ls: [sum(ls[i:]) for i in range(len(ls)+1)]



def parts_sums(ls):
    if len(ls) == 0:
        return [0]
    totalSum = sum(ls)
    sumList=[totalSum]
    for i in range(1, len(ls)+1):
        totalSum -= ls[i-1]
        sumList.append(totalSum)
    return sumList




print(parts_sums([0, 1, 3, 6, 10]))