def is_prime(num):
    if num <= 1: return False
    return len([i for i in range(2, int(num**0.5)+1) if num % i == 0]) == 0



# def is_prime(num):
#     if num > 1:
#         for i in range(2, int(num**0.5)+1):
#             print(i)
#             if num % i == 0:
#                 return False
#         return True
#     return False





print(is_prime(2))
print(is_prime(73))
print(is_prime(75))