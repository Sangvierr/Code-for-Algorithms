import sys

line = sys.stdin.readline().rstrip().split()
string = line[0]

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt=0
while string:
    found=False
    for c in croatia:
        if string.startswith(c):
            cnt+=1
            string=string[len(c):] # 찾은 부분은 삭제
            found=True
            break
    
    # 그냥 알파벳이라면 하나만 삭제
    if not found:
        cnt+=1
        string=string[1:]

print(cnt)