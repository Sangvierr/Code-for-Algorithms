import sys

sentence = sys.stdin.readline().rstrip()

words = sentence.split()
print(len(words))