# 1
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)


# 2
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))


# 3
lst = []
del lst
print(lst)


# 4
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)
