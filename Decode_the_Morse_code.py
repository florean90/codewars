def decodeMorse(morse_code):
    MORSE_CODE = {"....":"H",
                "-.--":"Y",
                ".---":"J",
                "..-":"U",
                "-..":"D",
                 ".":"E",
                  " ":" "
                }
    # result = []
    # for coded_word in morse_code.split("   "):
    #     word = ""
    #     for coded_char in coded_word.split():
    #         # for key in MORSE_CODE.keys():
    #         word += MORSE_CODE[coded_char]
    #     # print(word)
    #     result.append(word)
    # return " ".join(result).strip(" ")

    return " ".join("".join(MORSE_CODE[char] for char in word.split()) for word in morse_code.split("   ")).strip(" ")





    # # Todo: Accept dots, dashes and spaces, return human-readable message
    # return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')






a = '.... . -.--   .--- ..- -.. .'
print(decodeMorse(a))
#should return "HEY JUDE"