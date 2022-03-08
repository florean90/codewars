def solution(input):
    roman_numerals = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    if not input:
        return 0
    for char in roman_numerals:
        if input.startswith(char):
            return roman_numerals[char] + solution(input[len(char):])

# def solution(roman):
#     roman_numerals = {"I": 1,
#                       "V": 5,
#                       "X": 10,
#                       "L": 50,
#                       "C": 100,
#                       "D": 500,
#                       "M": 1000,
#                       "": 0
#                       }
#     roman = roman[::-1]
#     result = 0
#     for i in range(len(roman)):
#         if roman_numerals[roman[i]] >= roman_numerals[roman[i-1:i]]:
#             result += roman_numerals[roman[i]]
#         else:
#             result -= roman_numerals[roman[i]]
#     return result




print(solution('XXI'))