N = int(input())
lst = list(map(int, input().split()))
lst2 = sorted(list(set(lst)))

dic = {lst2[i] : i for i in range(len(lst2))}

for i in lst:
    print(dic[i], end=' ')