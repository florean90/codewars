def to_camel_case(text):
    return text[0] + text.title().translate(str.maketrans("","","-_"))[1:] if text else text





# def to_camel_case(text):
#     text = list(text)
#     result = ""
#     for i in range(len(text)):
#         if text[i] in ["-", "_"]:
#             text[i+1] = text[i+1].upper()
#             continue
#         result += text[i]
#     return result









a = "the-stealth-warrior"
print(to_camel_case(a))