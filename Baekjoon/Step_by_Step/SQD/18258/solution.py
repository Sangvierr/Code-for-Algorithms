import sys
T = int(sys.stdin.readline().rstrip())

queue = []

for _ in range(T):
    line = sys.stdin.readline().rstrip().split()

    if len(line) == 2:
        cmd, num = map(str, line)
        num = int(num)

        if cmd == 'push':
            queue.append(num)
    
    else:
        cmd = str(line[0])

        if cmd == 'pop':
            if not queue:
                print(-1)
            else:
                item = queue.pop(0)
                print(item)
        
        elif cmd == 'size':
            print(len(queue))

        
        elif cmd == 'empty':
            if not queue:
                print(1)
            else:
                print(0)
        
        elif cmd == 'front':
            if not queue:
                print(-1)
            else:
                print(queue[0])
        
        elif cmd == 'back':
            if not queue:
                print(-1)
            else:
                print(queue[-1])