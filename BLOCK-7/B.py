M, N = map(int, input().split())
mass = input().split()
otvet = []
for i in range(0, len(mass) // 2 + 1):
    mass2 = []
    for y in range(i + i - 1, i - 1, -1):
        mass2.append(mass[y])
    if mass[0:i] == mass2:
        otvet.append((len(mass) - len(mass2)))
print(*otvet[::-1])
