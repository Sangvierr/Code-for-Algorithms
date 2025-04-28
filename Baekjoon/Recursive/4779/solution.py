import sys

def cut(start,n):
    if n == 1:
        return
    for i in range(start + n//3, start +(n//3)*2): # 가운데 문자열을 공백으로
        result[i] = ' '
    cut(start, n//3) # 왼쪽 자르기
    cut(start + n//3 * 2, n//3) # 오른쪽 자르기

while True:
    try :
        N = int(sys.stdin.readline())
        result = ['-']*(3**N)
        cut(0,3**N)
        print(''.join(result))
    except EOFError:
        break