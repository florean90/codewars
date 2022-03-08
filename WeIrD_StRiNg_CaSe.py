def to_weird_case(string):
    words_list = string.split()
    result = []
    for word in words_list:
        new_word = ""
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        result.append(new_word)
    return " ".join(result)






print(to_weird_case('Weird string case'))