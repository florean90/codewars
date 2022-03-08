def delete_nth(order,max_e):
    result = []
    for motiv in order:
        if result.count(motiv) < max_e:
            result.append(motiv)
    return result




print(delete_nth([1,1,1,1],2))
print(delete_nth([20,37,20,21], 1))
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))
