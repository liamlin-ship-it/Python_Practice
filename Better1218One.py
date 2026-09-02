target = int(input())

num = list(map(int, input().split()))

counts = {}
for x in num:
    counts[x] = counts.get(x, 0) + 1

for x in num:
    counts[x] -= 1

    complement = target - x

    if counts.get(complement, 0) > 0:
        print(x, complement)
        break