chars = input().split()

n = len(chars)

for i in range(n):
    for j in range(i + 1, n):
        print(chars[i], chars[j])