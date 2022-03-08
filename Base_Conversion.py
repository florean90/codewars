


def convert(input, source, target):
    result = []
    input = int(input)
    while input:
        result.append(target[int(input % len(target))])
        input = input // len(target)
    result.reverse()
    print("".join(result))

    input = "".join(result)
    result = []
    input = int(input)
    i = 0
    while input:
        result.append(input % 10 * len(target) ** i)
        input = input // 10
        i += 1
    print(sum(result))
    return







bin      = '01'
oct      = '01234567'
dec      = '0123456789'
hex      = '0123456789abcdef'
allow    = 'abcdefghijklmnopqrstuvwxyz'
allup    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha    = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphanum = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(convert("15", dec, bin))
print(convert("15", dec, hex))




