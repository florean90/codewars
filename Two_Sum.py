def two_sum(numbers, target):

    for index1 in range(len(numbers)):
        for index2 in range(len(numbers)):
            if index1 != index2 and numbers[index1]+numbers[index2] == target:
                return (index1, index2)






print(two_sum([1,2,3], 4))
print(two_sum([2,2,3], 4))