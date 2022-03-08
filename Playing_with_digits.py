def dig_pow(n, p):
    total = 0
    for i, digit in enumerate(str(n)):
        total += int(digit)**(p+i)
    return total//n if (total/n).is_integer() else -1



a = "HOW R U"
print(dig_pow(46288, 3))
