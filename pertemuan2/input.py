import datetime

nama = input("Nama anda: ")
kota = input("Kota asal anda: ")
tahun_lahir = input("Tahun lahir anda: ")

tahun_sekarang = datetime.datetime.now().year

print(
    nama,
    "berasal dari",
    kota,
    "sekarang berumur",
    tahun_sekarang - int(tahun_lahir),
    "tahun.",
)
