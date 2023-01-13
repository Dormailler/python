# 거꾸로 해도 똑같은 문자열 구하기
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

'''
def solution(s):
    for i in range(len(s)//2):
        j = len(s) - 1 - i 
        if s[i] != s[j]:
            return -1
    return 1 

print(solution(input()))
'''
