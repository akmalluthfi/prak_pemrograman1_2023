num = int(input("Masukkan maks angka : "))

for i in range(1, num + 1):
    if i % 2 == 0:
        continue

    print(i)


print("")


i = 0
while i < num:
    i += 1

    if i % 2 == 0:
        continue

    print(i)
