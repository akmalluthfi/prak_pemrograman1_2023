subjects = []
semesters = []

while True:
    subject = input("Masukkan nama MK: ")

    if subject in subjects:
        print("MK sudah tersedia di dalam katalog")
        print("Mk tidak berhasil ditambahkan")
        continue

    semester = int(input("Masukkan semester pelaksanaan: "))

    if semester <= 0 or semester > 8:
        print("Semester yang tersedia untuk jenjang Sarjana Terapan adalah 1-8")
        print("Mk tidak berhasil ditambahkan")
        continue

    subjects.append(subject)
    semesters.append(semester)
    print(f"MK {subject} berhasil ditambahkan pada semester {semester}")

    next = input("Apakah masih ada MK yang akan dimasukkan (y/t)? ")
    print("")
    if next != "y":
        break


print("Daftar MK yang tersedia")
print("=" * 15)
for i in range(len(subjects)):
    print(f"{i + 1}. {subjects[i]} - Sem {semesters[i]}")
