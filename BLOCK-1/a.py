list_strok = []
n = int(input())

if 1 <= n <= 10**5:
    for i in range(n):
        list_strok.append(input()) # мой список из n строк
else:
    print('1<=n<=10**5')
print(list_strok)
# сортировка очереди  
i = 0  
while i < len(list_strok):
    if list_strok[i][0] == '-':
        list_strok.pop(i)
    elif list_strok[i][0] == '':
        list_strok.insert(len(list_strok)//2, list_strok.pop(i))
    elif list_strok[i][0] == '+':
        list_strok.append(list_strok.pop(i))
    else:
        i += 1

print(list_strok)
