num = list(map(int, input().split()))

x = int(input())

found = False

for i in range(len(num)):
    if num[i] == x:
        print(i)
        found = True
        
if not found:
    print(-1)