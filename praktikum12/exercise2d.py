nums = [i for i in range(1, 13)]


def graph(n):
    if n == 1:
        return 1
    elif n % 4 == 0:
        return -1 + graph(n - 1)
    else:
        return 1 + graph(n - 1)


result = map(lambda num: graph(num), nums)

print(nums)
print(list(result))
