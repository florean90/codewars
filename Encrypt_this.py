# def encrypt_this(text):
#     return " ".join(str(ord(word[0])) + word[-1:-2] + word[2:-1] + word[1:2] for word in text.split())



def encrypt_this(text):
    result = []
    for word in text.split():
        if len(word) > 2:
            result.append(str(ord(word[0])) + word[-1] + word[2:-1] + word[1])
        else:
            result.append(str(ord(word[0])) + word[1:])
    return " ".join(result)



print(encrypt_this("Hello world"))
print(encrypt_this("The more he saw the less he spoke"))
print(encrypt_this("A wise old owl lived in an oak"))
