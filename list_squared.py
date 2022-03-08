import time


def find_factors (number): # return an array of the factors (divisors) for each number
    factors = []
    for i in range(1, (int(number**0.5))+1):
        if number % i == 0:
            factors.append(i)
            factors.append(number//i)
    factors = list(set(factors))
    return factors


def sum_of_squared_factors(number): # return the sum of the squared factors
    result = 0
    for factor in find_factors(number):
        result += factor**2
    return result


def list_squared(m, n):
    result = []
    for number in range(m, n+1):
        total = sum_of_squared_factors(number)
        if (total ** 0.5).is_integer():
            result.append([number, total])
    return result



start = time.time()
print(list_squared(1, 10000))
# print(list_squared(246, 246))
# print(list_squared(9, 9))
print("#####################")
print(time.time()-start)
