# menus = ["Gado-gado", "Ayam rempah" "Takoyaki", "Jus buah", "Air mineral"]
# prices = [10_000, 10_000, 12_000, 6_000, 2_500]

menus = [
    ["Gado-gado", 10_000],
    ["Ayam rempah", 10_000],
    ["Takoyaki", 12_000],
    ["Jus buah", 6_000],
    ["Air mineral", 2_500],
]

print("Menu Kantin PENS")
for index, menu in enumerate(menus):
    print(f"{index + 1}. {menu[0]} \t Rp. {menu[1]}")

print("")

budget = int(input("Masukkan budget makan siang hari ini: "))

while True:
    selected_menu = int(input(f"Masukkan menu yang  ingin dipesan (1-{len(menus)}): "))

    # cek ketersediaan menu
    if selected_menu > len(menus) or selected_menu < 0:
        print("Pilihan tidak tersedia di menu, silahkan pilih lagi")
        continue

    menu = menus[selected_menu - 1]

    # cek budget
    if budget >= menu[1]:
        budget -= menu[1]
        print(f"{menu[0]} seharga {menu[1]} berhasil dipesan")
    else:
        print("Pemesanan tidak dapat diproses karena uang tidak mencukupi")

    print(f"Sisa budget adalah Rp. {budget}", end="\n\n")

    order_again = input("Ingin melakukan pemesanan lagi (y/t)? ")

    if order_again != "y":
        break

print("Program berakhir")
