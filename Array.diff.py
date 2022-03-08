def array_diff(a, b):
    return [i for i in a if b.count(i) == 0]











a = "recede"
print(array_diff([1,2,2,2,3],[2]))