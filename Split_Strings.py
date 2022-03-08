def solution(s):
    result = []
    if s not in ("", None):
        for i in range(0, len(s), 2):
            result.append(s[i:i+2])
        if len(result[-1]) < 2:
            result[-1] += "_"
    return result







print(solution("abcdefghi"))