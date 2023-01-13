a = []
def solution(s):
    for i in range(len(s)):
        j = len(s) - 1 - i 
        a.append(s[j])
    b = "".join(x for x in a)
    print(b)
    if b == s:
        return 1
    else:
        return -1

print(solution(input()))