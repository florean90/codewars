def longest_palindrome(s):
    max = 0
    for i in range(len(s)):
        for j in range(1, len(s[i:])+1):
            if s[i:][:j] == s[i:][:j][::-1]:
                if len(s[i:][:j]) > max:
                    max = len(s[i:][:j])
    return max




print(longest_palindrome("baablkj12345432133d"))
print(longest_palindrome("aa"))