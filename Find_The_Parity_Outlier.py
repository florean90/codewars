def find_outlier(integers):
    evenes = [i % 2 for i in integers]
    # print(evenes)
    return integers[evenes.index(True)] if evenes.count(True)==1 else integers[evenes.index(False)]





a = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(a))