import sys

n = sys.stdin.readline().rstrip().split(" ")

new_n1=''
for num in reversed(n[0]):
    new_n1+=num
    
new_n2=''
for num in reversed(n[1]):
    new_n2+=num

new_n1 = int(new_n1)
new_n2 = int(new_n2)

if new_n1 < new_n2:
    print(new_n2)   
else:
    print(new_n1)