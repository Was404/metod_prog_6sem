#BUG

num =9
ls = []
for i in range(50):
    c = input()
    ls.append(c)
for i in range(50):
    for i in range(len(ls)):
        if ls[i].startswith(str(num)):
            print(ls[i])
    num += 1