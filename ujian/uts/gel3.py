available_books = [
    "Atomic Habit",
    "Python Crash Course",
    "You Do You",
    "Laut Bercerita",
]

borrowed_books = []

print("Katalog Perpustakaan PENS (Maks. Peminjaman 2 Buku)")
print("=" * 20)
for i, book in enumerate(available_books):
    print(f"{i + 1}. {book}")

while True:
    borrowed_book = int(
        input(f"Masukkan buku yang ingin dipinjam 1-{len(available_books)} : ")
    )

    if borrowed_book > len(available_books) or borrowed_book < 0:
        print("Buku yang dipilih tidak tersedia pada katalog")
    elif available_books[borrowed_book - 1] in borrowed_books:
        print("Buku yang dipilih sudah kamu pinjam sebelumnya")
    else:
        borrowed_books.append(available_books[borrowed_book - 1])
        print(f"Buku {available_books[borrowed_book - 1]} berhasil dipinjam")
        print("")

        if len(borrowed_books) >= 2:
            print("Batas maksimum peminjaman sudah terpenuhi")
            print("Daftar buku yang dipinjam hari ini adalah", borrowed_books)
            break

        borrow_again = input("Apakah masih ada buku yang ingin dipinjam (y/t)? ")
        print("")
        if borrow_again != "y":
            print("Daftar buku yang dipinjam hari ini adalah", borrowed_books)
            break
