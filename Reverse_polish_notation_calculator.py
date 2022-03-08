# def calc(expr):
#     element_list = expr.split()
#     # print("element_list =", element_list)
#     if element_list == []:
#         return 0
#     if len(element_list) == 1:
#         return float(element_list[0])
#     for i in range(len(element_list)):
#         if element_list[i] in "+-*/":
#             if element_list[i] == "+":
#                 x = float(element_list[i - 2]) + float(element_list[i - 1])
#             elif element_list[i] == "-":
#                 x = float(element_list[i - 2]) - float(element_list[i - 1])
#             elif element_list[i] == "*":
#                 x = float(element_list[i - 2]) * float(element_list[i - 1])
#             elif element_list[i] == "/":
#                 x = float(element_list[i - 2]) / float(element_list[i - 1])
#             if len(element_list) > 3:
#                 return calc(" ".join(element_list[:i - 2] + [str(x)] + element_list[i + 1:]))
#             return x


# import operator
#
# def calc(expr):
#     OPERATORS = {"+": operator.add,
#                  "-": operator.sub,
#                  "*": operator.mul,
#                  "/": operator.truediv
#                  }
#     stack = [0]
#     for token in expr.split():
#         if token in OPERATORS:
#             op2, op1 = stack.pop(), stack.pop()
#             stack.append(OPERATORS[token](op1, op2))
#         elif token:
#             stack.append(float(token))
#     return stack.pop()


def calc(expr):
    OPERATORS = {"+": lambda x, y: x+y,
                 "-": lambda x, y: x-y,
                 "*": lambda x, y: x*y,
                 "/": lambda x, y: x/y
                 }
    stack = [0]
    for token in expr.split():
        if token in OPERATORS:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPERATORS[token](op1, op2))
        elif token:
            stack.append(float(token))
    return stack.pop()




print(calc("5 1 2 + 4 * + 3 - 2 /"))