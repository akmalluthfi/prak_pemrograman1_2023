nums = [i for i in range(1, 12)]


def graph(n):
    if n == 1:
        return n
    elif n % 3 == 0:
        return 2 + graph(n - 1)
    else:
        return 1 + graph(n - 1)


result = map(lambda num: graph(num), nums)

print(nums)
print(list(result))
