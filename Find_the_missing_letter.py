def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(ord(chars[n])+1)



# import string
#
# def find_missing_letter(chars):
#     if chars[0] in string.ascii_lowercase:
#         for i, letter in enumerate(chars):
#             if letter != string.ascii_lowercase[string.ascii_lowercase.index(chars[0])+i]:
#                 return string.ascii_lowercase[string.ascii_lowercase.index(chars[0])+i]
#     elif chars[0] in string.ascii_uppercase:
#         for i, letter in enumerate(chars):
#             if letter != string.ascii_uppercase[string.ascii_uppercase.index(chars[0])+i]:
#                 return string.ascii_uppercase[string.ascii_uppercase.index(chars[0])+i]





print(find_missing_letter(["a","b","c","d","f"]))
print(find_missing_letter(["b","d","e","f"]))