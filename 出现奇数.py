x = input()
x = input()
x = list(map(int, x.strip().split()))
res = {}
if x == []:
    exit()
for i in x:
    if i not in res:
        res[i] = 1
    else:
        res[i] += 1

for i,j in res.items():
    if j % 2 == 1:
        print(i)
        break