def abbreviate(s):
    replace = lambda word: word[0] + str(len(word) - 2) + word[-1] if len(word) > 3 else word
    result, word = "", ""
    for char in s:
        if char.isalpha():
            word += char
        else:
            result += replace(word) + char
            word = ""
    result += replace(word)
    return result






print(abbreviate("internationalization"))
print(abbreviate("elephant-ride"))