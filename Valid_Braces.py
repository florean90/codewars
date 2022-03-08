def validBraces(string):
  while '{}' in string or '()' in string or '[]' in string:
      string = string.replace('{}', '')
      string = string.replace('[]', '')
      string = string.replace('()', '')
  return string == ''


# def validBraces(string):
#     parantheses = brackets = curly_braces = 0
#     for i, brace in enumerate(string):
#         if brace == "(":
#             parantheses +=1
#         elif brace == ")":
#             parantheses -=1
#             if parantheses < 0 or string[i-1] == "[" or string[i-1] == "{":
#                 return False
#         elif brace == "[":
#             brackets +=1
#         elif brace == "]":
#             brackets -=1
#             if brackets < 0 or string[i-1] == "(" or string[i-1] == "{":
#                 return False
#         elif brace == "{":
#             curly_braces +=1
#         elif brace == "}":
#             curly_braces -=1
#             if curly_braces < 0 or string[i-1] == "[" or string[i-1] == "(":
#                 return False
#     if parantheses == 0 and brackets == 0 and curly_braces == 0:
#         return True
#     else:
#         return False




print(validBraces("(){}[]"))
print(validBraces("[(])"))
print(validBraces("}{"))
print(validBraces("(){()}[]"))
