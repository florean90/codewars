def duplicate_count(text):
    return len([char for char in set(text.lower()) if text.lower().count(char) > 1])




# def duplicate_count(text):
#     text = text.lower()
#     chars = "".join(set(text))
#     count = 0
#     for char in chars:
#         if text.count(char) > 1:
#             count += 1
#     return count
#







a = "Indivisibilities"
print(duplicate_count(a))