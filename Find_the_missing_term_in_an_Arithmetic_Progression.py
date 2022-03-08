# def find_missing(sequence):
#     diferences = [sequence[i+1]-sequence[i] for i in range(len(sequence)-1)]
#     print(diferences)
#     if max(diferences) > 0:
#         return sequence[diferences.index(max(diferences))]+min(diferences)
#     if max(diferences) < 0:
#         return sequence[diferences.index(min(diferences))]+max(diferences)


def find_missing(sequence):
    return int((sequence[0] + sequence[-1]) * (len(sequence) + 1) / 2 - sum(sequence))





print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))
print(find_missing([-1, -2, -3, -4, -6, -7, -8, -9]))
print(find_missing([1, 2, 3, 4, 6]))