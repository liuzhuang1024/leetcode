x = input()
y = input()
x = x.strip().split(',') + y.strip().split(',')
x = map(int, x)

print(','.join(
    map(str, sorted(x))
))
