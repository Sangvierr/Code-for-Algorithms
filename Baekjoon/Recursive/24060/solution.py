import sys

def merge_sort(A, start, end):
    global cnt, result
    if start < end:
        mid = (start+end) // 2
        merge_sort(A, start, mid)
        merge_sort(A, mid+1, end)
        merge(A, start, mid, end)

def merge(A, start, mid, end):
    global cnt, result
    i = start
    j = mid+1
    temp=[]
    while (i <= mid and j <= end):
        if A[i] <= A[j]:
            temp.append(A[i])
            i+=1
        else:
            temp.append(A[j])
            j+=1
    while (i <= mid):
        temp.append(A[i])
        i+=1
    while (j<=end):
        temp.append(A[j])
        j+=1
    
    i=start
    for k in range(len(temp)):
        A[i] = temp[k]
        i += 1
        cnt+=1
        if cnt == K:
            result = temp[k]


N, K = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
result = -1
merge_sort(A, 0, N - 1)
print(result)