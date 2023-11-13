nums = [3, 2, 1]


def box(n):
    a = n * 8

    if n == 1:
        return 8
    elif n == 2:
        return 8 + box(1)
    else:
        return a + box(n - 1)


result = map(lambda num: box(num), nums)

print(list(result))
