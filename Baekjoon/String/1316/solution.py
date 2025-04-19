import sys

T = int(sys.stdin.readline().rstrip())

result=0
for _ in range(T):
    line = sys.stdin.readline().rstrip().split()
    lst=[]
    prev=''
    cnt=0
    for l in line[0]:
        if l not in lst or l==prev:
            lst.append(l)
            prev=l
            cnt+=1  
        else:
            break

        if cnt==len(line[0]):
            result+=1

print(result)
