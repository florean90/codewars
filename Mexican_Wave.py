def wave(people):
    return [people[:i] + people[i].upper() + people[i+1:] for i in range(len(people)) if people[i].isalpha()]





# import string
#
#
# def wave(people):
#     result = []
#     for i in range(len(people)):
#         if people[i] in string.ascii_lowercase:
#             temp_wave = list(people)
#             temp_wave[i] = temp_wave[i].upper()
#             result.append("".join(temp_wave))
#     return result






print(wave("two words"))