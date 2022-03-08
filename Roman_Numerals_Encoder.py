def solution(n):
    roman_numerals = {1000: 'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
                      }
    roman_string = ''
    for key in sorted(roman_numerals.keys(), reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string



# def solution(n):
#     result = n//1000 * "M"
#     centuries =  n%1000//100
#     print(centuries)
#     if centuries == 9:
#         result += "CM"
#     elif 5 <= centuries < 9:
#         result += "D" + "C" * (centuries-5)
#     elif centuries == 4:
#         result += "CD"
#     elif centuries <= 3:
#         result += centuries * "C"
#
#     decades = n%100//10
#     if decades == 9:
#         result += "XC"
#     elif 5 <= decades < 9:
#         result += "L" + "X" * (decades-5)
#     elif decades == 4:
#         result += "XL"
#     elif decades <= 3:
#         result += decades * "X"
#
#     years = n%10
#     if years == 9:
#         result += "IX"
#     elif 5 <= years < 9:
#         result += "V" + "I" * (years-5)
#     elif years == 4:
#         result += "IV"
#     elif years <= 3:
#         result += years * "I"
#
#     return result



print(solution(1889))  #'MDCCCLXXXIX' MCMLXXXIX
print(solution(307))