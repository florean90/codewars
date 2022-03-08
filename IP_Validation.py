# import socket
#
# def is_valid_IP(addr):
#     try:
#         socket.inet_pton(socket.AF_INET, addr)
#         return True
#     except socket.error:
#         return False



def is_valid_IP(strng):
    strng_list = strng.split(".")
    passed = 0
    for sequence in strng_list:
        if sequence.isnumeric() and sequence[0] != "0" and 0 < int(sequence) <= 255:
            passed += 1
    return passed == 4




# def is_valid_IP(strng):
#     strng = strng.split(".")
#     if len(strng) == 4:
#         try:
#             for i in strng:
#                 if str(int(i)) == i and 0 <= int(i) <= 255:
#                     pass
#                 else: return False
#             return True
#         except:
#             return False
#     return False





print(is_valid_IP("12.255.56.1"))
print(is_valid_IP("123.456.789.0"))
print(is_valid_IP("192.168.0.1"))