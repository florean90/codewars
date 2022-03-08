# def dashatize(n):
#     if n == None:
#         return None
#     n = str(abs(n))
#     result = ""
#     for i in range(len(n)):
#         if int(n[i]) % 2 == 1 and i > 0 and result[-1] != "-":
#             result += "-"
#         result += n[i]
#         if int(n[i]) % 2 == 1 and i < len(n)-1:
#              result += "-"
#     return result

import re

def dashatize(n):
    if n == None:
        return "None"
    return "-".join(i for i in re.split("([13579])", str(abs(n))) if len(i)>0)







a = 88744566
print(dashatize(a))
print(dashatize(531122))