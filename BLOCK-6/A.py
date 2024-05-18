n, k, m = map(int, input().split())
mas = [k] * n

for _ in range(m):
    a, b = map(int, input().split())
    z = 0
    for j in range(a, b):
        if mas[j] == 0:
            z = 5
            break
    if z == 5:
        print('0')
    else:
        for j in range(a, b):
            mas[j] -= 1
        print('1')