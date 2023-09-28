n = int(input("Masukan jumlah data : "))
data = []

for i in range(1, n + 1):
    num = input(f"Data ke-{i} : ")
    data.append(num)

while True:
    print("")
    first_index = int(input("Index awal : "))
    last_index = int(input("Index akhir : "))

    if first_index < 0 or last_index < 0:
        print("Program hanya menerima index positif")
    elif first_index > last_index:
        print("Index awal harus lebih kecil daripada index akhir")
    elif last_index > len(data):
        print("Index melebihi panjang list")
    else:
        print(f"Data index ke-{first_index} s.d index ke-{last_index}")
        print(data[first_index : last_index + 1], end="\n\n")

        input_again = input("Ulangi lagi (y/t) : ")
        if input_again != "y":
            break
