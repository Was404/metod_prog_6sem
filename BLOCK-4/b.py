'''
Входные данные

В первой строке входных данных содержатся два числа: N и M (1 <= N,M <= 100), где N – количество ОВП, а M – количество пар ОВП, 
которые не могут сидеть за одним столом. В следующих M строках записано по 2 числа – пары ОВП, которые не могут сидеть за одним столом.

Выходные данные
Если способ рассадить ОВП существует, то  выведите YES в первой строке и номера ОВП, которых необходимо посадить за первый стол, 
во второй строке. В противном случае в первой и единственной строке выведите NO.

'''
#БАНКЕТ
N,M=[int(i) for i in (input().split())]
pairs=[input().split() for i in range(M)]
for pair in (pairs):
    pair[0]=int(pair[0])
    pair[1]=int(pair[1])


color=[0]*N
# for i in range(len(color)): color.append(0)
# print(color)
# print(pairs)

def analiz(t,  color):  # в этой рекурсивной функции будем пробовать рассаживать (красить)
    for i in range(t, M): # начиная с пары врагов t
        a = pairs[i][0]
        b = pairs[i][1]
        # print(i)
        if (color[a - 1] == 0):    # первый не окрашен
            if (color[b - 1] == 0):   # второй тоже не окрашен
                color[a - 1] = 1   # попробуем такой вариант раскраски
                color[b - 1] = -1
                if (analiz(i+1, color)==False): # если не получилось, раскрасим наоборот
                    color[a - 1] = -1
                    color[b - 1] = 1
                    # print(color)
                    return analiz(i+1, color) # и вернем результат
            else:
                color[a - 1] = -color[b - 1]; # за другой стол, овп №1 из пары
                # print(color)
        else: # первый окрашен
            if (color[b - 1] == 0): # если первый окрашен, а второй не окрашен
                    color[b - 1] = -color[a - 1]; # за другой стол овп №2 из пары
            else: # второй тоже
                    if (color[b - 1] == color[a - 1]): # скандал
                        return False
    # print(color)
    return True



if (analiz(0,color) or N < 2):
    print("YES")
    ans=[]
    if (N >= 2):
        for i in range(N):
            if color[i] == 1:
                ans.append(str(i+1))
        full_data = ' '.join(ans)
        print(full_data)
    else:
        print('1')  
else:
    print("NO")
# print(color)