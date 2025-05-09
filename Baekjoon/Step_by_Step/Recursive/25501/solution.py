import sys

T = int(sys.stdin.readline().rstrip())

def recursion(s, l, r):
    global call_cnt
    call_cnt+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(T):
    call_cnt = 0
    string = sys.stdin.readline().rstrip()
    print(isPalindrome(string), call_cnt)