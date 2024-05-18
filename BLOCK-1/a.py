list_strok = []
TRAIN_LIST = ['+ 1', '+ 2', '-', '+ 3', '+ 4', '-', '-']

# сортировка очереди  

def metod1(list_strok):
    i = 0  
    while i < len(list_strok): #BUG
        if list_strok[i][0] == '-':
            list_strok.pop(i)
        elif list_strok[i][0] == '':
            list_strok.insert(len(list_strok)//2, list_strok.pop(i))
        elif list_strok[i][0] == '+':
            list_strok.append(list_strok.pop(i))
        else:
            i += 1
    print(list_strok)

def metod2(list_strok):
    # Отсортировать список с учетом указанных условий
    sorted_list = sorted(list_strok, key=lambda x: (x[0] == '+' and 1) or (x[0] == '*') or 0)

    # Удалить первое значение списка, если оно начинается с минуса
    if sorted_list[0][0] == '-':
        del sorted_list[0]

    # Найти индекс, где вставить значения, начинающиеся с '*'
    insert_index = sorted_list.index(next(x for x in sorted_list if x[0] == '*'))

    # Вставить значения, начинающиеся с '*', в середину списка
    list_strok.insert(insert_index, '* new_value')

    print(sorted_list)

metod2(TRAIN_LIST)
n = int(input())
if 1 <= n <= 10**5:
    for i in range(n):
        list_strok.append(input()) # мой список из n строк
else:
    print('1<=n<=10**5')
print(list_strok)
