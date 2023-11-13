nums = [3, 2, 1]


def checkbox(n):
    a = n * 4

    if n == 1:
        return a
    else:
        return a + checkbox(n - 1)


result = map(lambda num: checkbox(num), nums)

print(nums)
print(list(result))
