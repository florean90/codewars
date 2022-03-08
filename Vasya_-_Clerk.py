def tickets(people):
    n25=n50=0
    for customer in people:
        if customer == 25                 :n25 +=1
        elif customer == 50               :n50 +=1; n25 -=1
        elif customer == 100 and n50 > 0  :n25 -=1; n50 -=1
        elif customer == 100 and n50 == 0 :n25 -=3
        print(n25, n50)
        if n25 < 0 or n50 < 0:
            return "NO"
    return "YES"





# def tickets(people):
#     bank = []
#     for i in range(len(people)):
#         bank.append(people[i])
#         if people[i] == 50:
#             try:
#                 bank.remove(25)
#             except:
#                 return "NO"
#         elif people[i] == 100:
#             try:
#                 bank.remove(25)
#             except:
#                 return "NO"
#             try:
#                 bank.remove(50)
#             except:
#                 try:
#                     bank.remove(25)
#                     bank.remove(25)
#                 except:
#                     return "NO"
#     print(bank)
#     return "YES"





a = [25, 100]
print(tickets(a))