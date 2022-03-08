def sort_array(source_array):
  odds = sorted((x for x in source_array if x % 2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in source_array]







# def sort_array(source_array):
#     index_array = []
#     odd_array = []
#     for i, number in enumerate(source_array):
#         if number % 2 == 1:
#             index_array.append(i)
#             odd_array.append(number)
#     odd_array.sort()
#     for i in range(len(odd_array)):
#         source_array[index_array[i]] = odd_array[i]
#     return source_array









print(sort_array([5, 8, 6, 3, 4]))
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))