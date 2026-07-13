import math

s1, s2, s3 = input().split()

n1 = float(s1)
n2 = float(s2)
n3 = float(s3)

ceil1 = math.ceil(n1)
ceil2 = math.ceil(n2)
ceil3 = math.ceil(n3)

d1 = ceil1 - n1
d2 = ceil2 - n2
d3 = ceil3 - n3

subMin = min([d1, d2, d3])

if subMin == d1:
    print(s1)
elif subMin == d2:
    print(s2)
else:
    print(s3)
