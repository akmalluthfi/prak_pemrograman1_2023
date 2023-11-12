# 1 : create lambda
is_even = lambda num: num % 2 == 0
print(is_even(5))
print(is_even(10))


# 2 : lambda using user defined function
def apply_operation(value1, value2, operation):
    return operation(value1, value2)


addition = apply_operation(5, 100, lambda operand1, operand2: operand1 + operand2)
print("5 + 100 =", addition)
multiplication = apply_operation(5, 100, lambda operand1, operand2: operand1 * operand2)
print("5 * 100 =", multiplication)

# 3 : lambda using built in function
numbers = [x for x in range(1, 25)]
even_numbers = filter(lambda num: num % 2 == 0, numbers)

print(list(even_numbers))
