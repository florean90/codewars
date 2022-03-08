def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)






# def create_phone_number(n):
#     n.insert(0, "(")
#     n.insert(4, ") ")
#     n.insert(8, "-")
#     return "".join(str(i) for i in n)





a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(a))