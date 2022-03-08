def iq_test(numbers):
    evenes = [int(i) % 2 == 0 for i in numbers.split()]
    return evenes.index(True) + 1 if evenes.count(True) == 1 else evenes.index(False) + 1







a = '2 4 7 8 10'
print(iq_test(a))