import time

def decompose(n):
    n2 = n**2
    compositors = []
    for i in reversed(range(n)):
        compositors.append(i ** 2)
    print(f"Initial compositors {compositors}")

    temp_compositors = [i for i in compositors]
    count = 0

    while True:
        count += 1
        # print(f"count = {count}")
        result = temp_compositors[:count]
        print(f"resultatul = {result} = {sum(result)}")
        if sum(result) > n2:
            temp_compositors[count - 1] = 0
            continue
        elif sum(result) < n2:
            if count == len(temp_compositors):
                for i in range(1, len(temp_compositors)):
                    if temp_compositors[i] > 0:
                        temp_compositors[i] = 0
                        for x in range(i + 1, len(temp_compositors)):
                            temp_compositors[x] = compositors[x]
                        break
                if sum(temp_compositors) == 0:
                    return None
                if sum(temp_compositors[1:]) == 0:
                    temp_compositors = [i for i in compositors]
                    temp_compositors[0] = 0
                count = 0
            continue
        elif sum(result) == n2:
            # print("Evrica!")
            break
        break

    print("##############")
    print(f"{sum(result)} need to be equal {n ** 2}")
    print(result)
    return [int(i ** 0.5) for i in reversed(result) if i != 0]




start = time.time()

a = 12
print(decompose(a))

print("#####################")
print(time.time()-start)