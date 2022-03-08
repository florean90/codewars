def comp(array1, array2):
    try:
        return sorted(i**2 for i in array1) == sorted(array2)
    except:
        return False





# def comp(array1, array2):
#     if array1 == None or array2 == None:
#         return False
#     if len(array1) == 0 and len(array2) == 0:
#         return True
#     if len(array1) == 0 or len(array2) == 0:
#         return False
#     for i in array1:
#         if i**2 not in array2:
#             return False
#         array2.remove(i**2)
#     return True






a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a, b))