def find_even_index(arr):
    for i in range(len(arr)):
        # print(sum(arr[i+1:]))
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1




a = [2,2,3,-3,-4,1]
print(find_even_index(a))