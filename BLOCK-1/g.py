N = int(input())
for i in range(N):
    a, b = list(map(int, input().split()))
    if b <= 30 and b < 60:
        b += 30
        if b == 60:
            a += 1
            b -= 60
        print(a,b)
    elif a < 12:
        b = b - 30
        a += 1
        if a == 12:
            a = 0
        print(a,b)