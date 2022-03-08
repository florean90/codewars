import re

def count_smileys(arr):
    return len(list(re.findall(r"[:;][-~]?[)D]"," ".join(arr))))




# def count_smileys(arr):
#     count = 0
#     for smile in arr:
#         if smile[0] == ":" or smile[0] == ";":
#             if smile[1] == ")" or smile[1] == "D":
#                 count += 1
#             elif smile[1] == "-" or smile[1] == "~":
#                 if smile[2] == ")" or smile[2] == "D":
#                     count += 1
#     return count







print(count_smileys([';D', ':-(', ':-)', ';~)']))