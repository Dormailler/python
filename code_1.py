def solution(msg):
    dic = {}
    stack = []
    num = 1
    for i in range(65,91):
        dic[chr(i)] = num
        num += 1
    for i in range(3):
        n = 1
        while msg[i:i+n] in dic:
            if i+n+1 >= len(msg):
                break
            n += 1
        if n > 1:
            stack.append(dic[msg[i:i+n-1]])
        dic[msg[i:i+n]] = num
        num += 1
    print(dic)
    return stack
print(solution('KAKAO'))