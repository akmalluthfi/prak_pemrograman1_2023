nums = [i for i in range(1, 11)]


def recursive1(n):
    if n == 1:
        return 1
    elif n % 3 == 0:
        return (n - 1) + recursive1(n - 2)
    else:
        return n + recursive1(n - 1)


result1 = map(lambda num: recursive1(num), nums)

print(nums)
print(list(result1))

print("=" * 10)


def recursive2(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return recursive2(n - 1)
    else:
        return n * recursive2(n - 1)


result2 = map(lambda num: recursive2(num), nums)

print(nums)
print(list(result2))
