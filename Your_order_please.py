def order(sentence):
    return " ".join(sorted(sentence.split(), key = lambda word: sorted(word)))



# def order(sentence):
#     result = []
#     sentence = sentence.split()
#     for i in range(len(sentence)):
#         for word in sentence:
#             if str(i+1) in word:
#                 result.append(word)
#     return " ".join(result)




a = "is2 Thi1s T4est 3a"
print(order(a))