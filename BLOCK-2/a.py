def foo(s, d=0):
    global s_set
    if d == 6:
        s_list = list(s)
        s_list[0], s_list[3] = s_list[3], s_list[0]
        s_set.add("".join(s_list))
        s_list[0], s_list[3] = s_list[3], s_list[0]
        return

    for i in range(d, 3 if d < 3 else 6):
        s_list = list(s)
        s_list[d], s_list[i] = s_list[i], s_list[d]
        foo("".join(s_list), d + 1)
        s_list[d], s_list[i] = s_list[i], s_list[d]


if __name__ == "__main__":
    s = input()
    s_set = set()

s_list = list(s)
s_list[0], s_list[3] = s_list[3], s_list[0]
foo("".join(s_list))

print(len(s_set))
for val in s_set:
    print(val)
