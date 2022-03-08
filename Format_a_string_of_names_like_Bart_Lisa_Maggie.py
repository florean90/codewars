def namelist(names):
    if len(names) == 1:
        return names[0]["name"]
    elif len(names) > 1:
        return "{} & {}".format(", ".join(name["name"] for name in names[:-1]), names[-1]["name"])
    else:
        return ""


# def namelist(names):
#     names_list = []
#     for x in names:
#         for name in x.values():
#             names_list.append(name)
#     result = ""
#     if len(names_list) == 1:
#         result = names_list[0]
#     if len(names_list) == 2:
#         result = (f"{names_list[0]} & {names_list[1]}")
#     if len(names_list) > 2:
#         for i in range(len(names_list)-2):
#             result += (f"{names_list[i]}, ")
#         result += (f"{names_list[-2]} & {names_list[-1]}")
#     return result



print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]))
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ]))
print(namelist([ {'name': 'Bart'} ]))
print(namelist([ ]))