# Program menampilkan urutan angka dari 1 ke n
# dan tanpa menampilkan beberapa angka10

num = int(input("Masukkan maksimal angka untuk di loop : "))
num_skips = input("Masukkan angka yang ingin di skip (1,2,...): ")

num_skips = str.split(num_skips, ",")

# for i in range(1, num + 1):
#     if str(i) in num_skips:
#         continue

#     print(i)
for i in range(1, num + 1):
    if str(i) not in num_skips:
        print(i)
