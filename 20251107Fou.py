s = input().strip()

data = list(map(int, input().split()))

k = data[0]
indicies = data[1:]

chars= list(s)

for idx in indicies:
    chars[idx] += '.'

print("".join(chars))