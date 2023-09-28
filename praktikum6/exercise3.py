# Program simple TODO list
tasks = []
menu = "1"

while True:
    if menu == "1":
        task = input("Tambahkan Tugas : ")
        tasks.append(task)
        print("Tugas berhasil ditambahkan")
    elif menu == "2":
        task = input("Tugas yang ingin dihapus : ")

        if task in tasks:
            tasks.remove(task)
            print("Tugas berhasil dihapus")
        else:
            print("Tugas tidak ditemukan")

    tasks.sort()
    print("\nList Tugas :")
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

    if menu == "3":
        print("\nProgram selesai")
        break

    print("\nApakah yang ingin anda lakukan selanjutnya")
    print("1. Menambahkan tugas")
    print("2. Menghapus tugas")
    print("3. Keluar")

    while True:
        menu = input("Masukkan pilihan (1/2/3) : ")
        print("")
        if menu == "1" or menu == "2" or menu == "3":
            break
