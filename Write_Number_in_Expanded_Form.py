def expanded_form(num):
    num = str(num)
    return " + ".join([num[i] + "0"*(len(num)-i-1) for i in range(len(num)) if num[i] != "0"])











print(expanded_form(70304))