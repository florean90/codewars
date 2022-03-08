def tribonacci(signature, n):
    while len(signature) < n:
            signature.append(sum(signature[-3:]))
    return signature[:n]





# def tribonacci(signature, n):
#     result = [signature[i] for i in range(min(3, n))]
#     while len(result) < n:
#         result.append(sum(result[-3:]))
#     return result







a = [1, 1, 1]
print(tribonacci(a, 10))