def meeting(s):
    return ''.join(f'({last_name}, {first_name})' for last_name, first_name in sorted(name.split(':')[::-1] for name in s.upper().split(';')))


# def meeting(s):
#     name_list = sorted(s.upper().split(";"))
#     reversed_list = []
#     for person in name_list:
#         first_name, last_name = person.split(":")[0], person.split(":")[1]
#         reversed_list.append(f"{last_name}, {first_name}")
#     return "".join(f"({i})" for i in sorted(reversed_list))

# from collections import OrderedDict

# def meeting(s):
#     name_list = s.split(";")
#     name_dict = {}
#     for name in name_list:
#         first_name, last_name = name.split(":")[0].upper(), name.split(":")[1].upper()
#         name_dict[first_name] = last_name
#     name_dict = OrderedDict(sorted(name_dict.items()))
#     name_dict = sorted(name_dict.items(), key=lambda item: item[1])
#     return "\n".join(f"({first_name}, {last_name})" for last_name, first_name in name_dict)




print(meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))
print(meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"))