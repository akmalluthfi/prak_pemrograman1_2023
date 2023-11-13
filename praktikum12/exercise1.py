from functools import reduce

# Example Map 1
days = ["senin", "selasa", "rabu", "kamis", "jum'at"]
capitalize_days = map(lambda day: day.capitalize(), days)
print(list(capitalize_days))

# Example Map 2
words = ["sandhika", "erik", "doddy"]
word_lengths = map(lambda word: len(word), words)
print(list(word_lengths))

# Example Filter 1
fruits = ["apple", "banana", "cherry", "watermelon", "elderberry"]
short_fruits = filter(lambda fruit: len(fruit) < 7, fruits)
print(list(short_fruits))

# Example Filter 2
numbers = [-3, -2, -1, 0, 1, 2, 3]
positive_numbers = filter(lambda num: num > 0, numbers)
print(list(positive_numbers))

# Example Reduce 1
numbers2 = [1, 2, 3, 4, 5]
total = reduce(lambda accumulator, currentValue: accumulator + currentValue, numbers2)
print(total)

# Example Reduce 2
factorial = reduce(lambda acc, curr: acc * curr, numbers2)
print(factorial)
