layout = ["1", "ABC2", "DEF3",
       "GHI4", "JKL5", "MNO6",
      "PQRS7", "TUV8", "WXYZ9",
        "*",   " 0",    "#"]

def presses(phrase):
    result = 0
    for char in phrase.upper():
        for button in layout:
            if char in button:
                result += button.find(char)+1
    return result





# def presses(phrase):
#     result = 0
#     for i in phrase.lower():
#         print(ord(i))
#         if "a" <= i <= "o":
#             result += (ord(i)-97) % 3 + 1
#             # print((ord(i)-97)%3+1)
#         elif "p" <= i <= "s":
#             result += (ord(i) - 112) % 4 + 1
#             # print((ord(i)-112)%4+1)
#         elif "t" <= i <= "v":
#             result += (ord(i) - 116) % 3 + 1
#             # print((ord(i)-116)%3+1)
#         elif "w" <= i <= "z":
#             result += (ord(i) - 119) % 4 + 1
#             # print((ord(i)-119)%4+1)
#         elif i == "1" or i == " " or i == "*" or i == "#":
#             result += 1
#         elif "2" <= i <= "6" or i == "8":
#             result += 4
#         elif i == "7" or i == "9":
#             result += 5
#         elif i == "0":
#             result += 2
#         print(result)
#
#     return result







a = "HOW R U"
print(presses(a))
