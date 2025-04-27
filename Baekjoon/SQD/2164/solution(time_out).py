import sys

N = int(sys.stdin.readline().rstrip())

lst = [i+1 for i in range(N)]
finished = False

while len(lst)>1:
    for cmd in ['drop', 'go-back']:
        if not lst:
            break

        if cmd == 'drop':
            lst.pop(0)
        elif cmd == 'go-back':
            first_elem = lst.pop(0)
            lst.append(first_elem)
    
    if not lst:
        break

if lst:
    print(lst[0])