words = input()

num = int(input())

numbers = list(map(int, input().split()))

codebook = ""

for i in numbers:
    codebook += words[i]

print(codebook)