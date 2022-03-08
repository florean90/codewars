def sum_dig_pow(a, b):
    return [number for number in range(a, b+1) if number == sum(int(str(number)[i])**(i+1) for i in range(len(str(number))))]




print(sum_dig_pow(1, 100))