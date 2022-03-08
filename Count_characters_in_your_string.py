def count(string):
    return {char: string.count(char) for char in string}

import collections
print(count("aba"))