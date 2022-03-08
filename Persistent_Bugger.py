def persistence(n):
    n_str = str(n)
    count = 0
    next_n = n
    while next_n >= 10:
        next_n = 1
        for i in n_str:
            next_n *= int(i)
        n_str = str(next_n)
        print(n_str)
        count += 1
    return count




a = 999

print(persistence(a))
