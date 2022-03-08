import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())


# import string
#
# def is_pangram(s):
#     s = s.lower()
#     filtred = ""
#     for char in s:
#         if char in string.ascii_lowercase and char not in filtred:
#             filtred += char
#     return len(filtred) == 26






print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
