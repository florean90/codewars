array = [1, 10, 9, 12, 3, 4]

def thirt(n):
    result = 0
    for i, c in enumerate(reversed(str(n))):
        result += int(c) * array[i%6]
    if result == n:
        return result
    return thirt(result)





a = 8529
print(thirt(a))
