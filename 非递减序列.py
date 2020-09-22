x = list(map(int, input().split()))

pre = x[0]
cur = x[1]
flag = 0
for i in range(2, len(x)):
    if pre <= cur:
        pre, cur = cur, x[i]
    else:
        pre, cur = cur, x[i]
        flag += 1
if flag >= 2:
    print(0)
else:
    print(1)
