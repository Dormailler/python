a,b = map(int,input().split())
a,b = list(str(a)),list(str(b))
c = []
stack = 0
for i in range(len(a)-1,-1,-1):
    if (int(a[i])+int(b[i])+stack) >= 10:
        c.insert(0,int(a[i])+int(b[i])+stack-10)
        stack = 1
        if(stack == 1 and i == 0):
            c.insert(0,1)
    else:
        c.insert(0,int(a[i])+int(b[i])+stack)
        stack = 0
out = ''.join(str(s) for s in c)
print(out)
    









    


