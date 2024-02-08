'''
Входные данные

На вход программы поступает  одна строка, которая представляет собой корректный автомобильный номер.

Выходные данные

В первой строке  выведите число k – количество номеров, которые могут получиться из заданного перестановкой букв и/или цифр.
В последующих k строках выведите все такие номера в произвольном порядке.
'''
# import array as arr
import itertools
# k = int(input())
list123 = []
listABC = []
nomerok = input()
n = 1
chunks = [nomerok[i:n+i] for i in range(0, len(nomerok), n)]
chunks = list(chunks)
for i in range(6):
    try:
        chunks[i] = int(chunks[i])
        list123.append(chunks[i])
    except:
        listABC.append(chunks[i])

#print(nomerok, list123, listABC)
list123 = list(map(str, list123)) # из цыфр в строки
#делаем комбинации itertools
comb_list123 = itertools.permutations(list123)
comb_listABC = itertools.permutations(listABC)
# массивы
arr_comb_listABC = []
arr_comb_list123 = []

num = ''
list_num = []

for i in comb_listABC:
    arr_comb_listABC.append([i[0], i[1], i[2]])

for i in comb_list123:
    arr_comb_list123.append([i[0], i[1], i[2]])

for i in arr_comb_listABC:
    for j in arr_comb_list123:
        num += i[0] + j[0] + j[1] + j[2] + i[1] + i[2]
        list_num.append(num)
        num = ''
list_num = list(set(list_num))
print(len(list_num))
for i in range(len(list_num)):
    print(list_num[i])

