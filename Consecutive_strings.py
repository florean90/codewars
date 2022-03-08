def longest_consec(strarr, k):
    result = ""
    lenght = 0
    if k > 0 and len(strarr) > 0:
        for i in range(len(strarr)-k+1):
            combination = "".join(strarr[i:i+k])
            if len(combination) > lenght:
                lenght = len(combination)
                result = combination
    return result










print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], 2))
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 5))