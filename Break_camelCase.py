def solution(s):
    return "".join(" "+i if i.isupper() else i  for i in s)



a = "helloWorld"

print(solution(a))
