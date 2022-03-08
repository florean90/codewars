def decrypt(encrypted_text, n):
    if encrypted_text in ("", None):
        return encrypted_text
    for i in range(n):
        encrypted_text1 = encrypted_text[len(encrypted_text)//2:]
        encrypted_text2 = encrypted_text[:len(encrypted_text)//2]
        encrypted_text = "".join(encrypted_text1[i:i+1] + encrypted_text2[i:i+1] for i in range(len(encrypted_text)//2+1))
    return encrypted_text


# def decrypt(encrypted_text, n):
#     if n > 0:
#         decrypted_text = ""
#         decrypted_text1 = [i for i in encrypted_text[int(len(encrypted_text) / 2):]]
#         decrypted_text2 = [i for i in encrypted_text[:int(len(encrypted_text)/2)]]
#         decrypted_text1.reverse()
#         decrypted_text2.reverse()
#         while len(decrypted_text1) > 0 or len(decrypted_text1) > 0:
#             if len(decrypted_text1) > 0:
#                 decrypted_text += decrypted_text1.pop()
#             if len(decrypted_text2) > 0:
#                 decrypted_text += decrypted_text2.pop()
#         return decrypt(decrypted_text, n-1)
#     return encrypted_text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text

# def encrypt(text, n):
#     if n > 0:
#         text = "".join([text[i] for i in range(1, len(text), 2)] + [text[i] for i in range(0, len(text), 2)])
#         return encrypt(text, n-1)
#     return text



print(encrypt("This is a test!!", 2))
print(decrypt("s e!ist!hi tT as", 2))