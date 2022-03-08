def revrot(strng, sz):
    if sz <= 0 or strng in ("", None):
        return ""
    result = ""
    for i in range(0, len(strng), sz):
        chunk = strng[i:i+sz]
        if len(chunk) == sz:
            if sum(int(i)*3 for i in chunk) % 2 == 0:
                result += chunk[::-1]
            else:
                result += chunk[1:]+chunk[0]
    return result




print(revrot("66443875", 4))