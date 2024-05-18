k = int(input())
s = input()
ex, res = 0, 0
for i in range(len(s) - k - 1, -1, -1):
    if s[i] == s[i + k]:
        ex += 1
    else:
        ex = 0
    res += ex
print(res)
