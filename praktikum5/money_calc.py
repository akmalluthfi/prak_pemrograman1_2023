print("Program menghabiskan uang")
init_money = int(input("Masukkan uang awal : "))

for i in range(1, 100):
    price = int(input("Masukkan harga barang : "))

    init_money -= price

    if init_money < 0:
        print("Uang anda sudah habis")
        print("Anda memiliki hutang", init_money)
        break
