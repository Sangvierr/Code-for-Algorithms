import sys
import queue

N = int(sys.stdin.readline().rstrip())

q = queue.Queue()
for i in range(1, N + 1):
    q.put(i)

while q.qsize() > 1:
    # drop => 맨 앞 삭제
    if not q.empty():
        q.get()

    # go-back => 맨 앞 삭제 후 맨 뒤로
    if q.qsize() > 1:
        if not q.empty():
            front = q.get()
            q.put(front)

if not q.empty():
    print(q.get())