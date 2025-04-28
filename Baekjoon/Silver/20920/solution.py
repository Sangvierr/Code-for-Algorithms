# 1. 자주 나옴
# 2. 길이가 길수록
# 3. 알파벳 사전순

import sys

N, M = map(int, sys.stdin.readline().split())

# 단어장 만들기
words = {}
for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if len(word) >= M:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

# 우선 순위에 따른 정렬
srt_words = sorted(words.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))

words_lst = [word for word, cnt in srt_words]

for s in words_lst:
    print(s)

