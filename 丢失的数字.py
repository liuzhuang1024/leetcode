x = list(map(int, input().strip().split(',')))
for i in range(x[-1]):
    if i == x[0]:
        x.pop(0)
        if x == []:
            break
    else:
        print(i)


