'''
Входные данные
Программа получает на вход целое число S — вместимость рюкзака, не превосходящее 10000 и количество слитков N, не превосходящее 300. 
Далее следует N целых неотрицательных чисел, не превосходящих 100000 — веса слитков.

Выходные данные
Программа должна вывести единственное целое число — максимально возможных вес золота, который поместится в данный рюкзак.

'''

S, N = map(int, input().split()) # N - количество слитков S - предел рюкзака
A = [int(i) for i in input().split()]

backpack = list()

for i in range(len(A)):
    if A[i] < S:
        backpack.append(A[i])
min = S
#print(backpack)
for i in range(len(backpack)):
    if backpack[i] < min:
        min = backpack[i]
        #print(min)

for i in range(N):
    if (min + backpack[i]) < S and min != backpack[i]:
        otvet = min + backpack[i]
print(otvet)