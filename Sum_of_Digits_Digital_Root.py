# def digital_root(n):
#     result = 0
#     for i in str(n):
#         result += int(i)
#     if result < 10:
#         return result
#     else:
#         return digital_root(result)


def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))



a = 493193
print(digital_root(a))