def count_bits(n):
    return sum(int(i) for i in bin(n)[2:])










a = 1234
print(count_bits(a))