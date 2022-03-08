def validate(n):
    n = str(n)
    if len(n) % 2 == 1:
        n = "0" + n
    final_number = []
    for i, digit in enumerate(n):
        digit = int(digit)
        if i % 2 == 0:
            if digit * 2 > 9:
                final_number.append(digit*2-9)
            else:
                final_number.append(digit*2)
        else:
            final_number.append(digit)
    print(final_number)
    return sum(final_number) % 10 == 0




print(validate(2121))