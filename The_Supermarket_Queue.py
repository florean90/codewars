def queue_time(customers, n):
    tills = [0]*n
    for customer in customers:
        tills[tills.index(min(tills))] += customer
        # print(tills)
    return max(tills)








a = "the-stealth-warrior"
print(queue_time([10,2,3,3], 2))