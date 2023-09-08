# Program untuk menentukan bil ganjil / genap

# menerima masukkan menggunakan fungsi input()
# lalu mengubah input menjadi integer menggunakan int()
# lalu menyimpan ke dalam variabel num
num = int(input("Masukkan bilangan : "))

# cek jika num dibagi 2 sisa 0
if num % 2 == 0:
    # jika iya maka print genap
    print("Bilangan", num, "Adalah bilangan genap!")
else:
    # jika tidak maka print ganjil
    print("Bilangan", num, "adalah bilangan ganjil!")
