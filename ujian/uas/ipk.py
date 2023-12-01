students = []


def input_nrp():
    while True:
        nrp = input("\nMasukkan nrp mahasiswa: ")

        found = False
        for student in students:
            if nrp == student["nrp"]:
                found = True
                break

        if not found:
            return nrp

        print("NRP sudah tersedia")


def input_scores():
    print("\nMasukkan nilai mahasiswa dari semester 1 - 8")
    print("Pisahkan nilai menggunakan koma")
    print("cth: 3.2, 4.4, ...")

    while True:
        scores = input("Masukkan nilai mahasiswa: ")
        scores = scores.strip(",")
        scores_list = [float(score) for score in scores.split(",")]

        if len(scores_list) != 8:
            print("Masukkan nilai 8 semester")
            print("Nilai yang dimasukkan =", len(scores_list))
            continue

        safe = True
        for score in scores_list:
            if not (0 <= score <= 4):
                safe = False
                break

        if not safe:
            print("Nilai semester range dari 0 - 4")
            continue

        return scores_list


def add_student():
    student_nrp = input_nrp()
    student_name = input("Masukkan nama mahasiswa: ")
    student_scores = input_scores()

    students.append(
        {
            "nrp": student_nrp,
            "name": student_name,
            "scores": student_scores,
            "ipk": sum(student_scores) / len(student_scores),
        }
    )

    print("Berhasil menambahkan mahasiswa")


def show_students():
    print("\nList mahasiswa")

    sorted_students = sorted(students, key=lambda student: student["ipk"], reverse=True)

    for student in sorted_students:
        print(
            f"{student['nrp']} - {student['name']} - {student['ipk']}",
            "(cumlaude)" if student["ipk"] > 3.5 else "",
        )


while True:
    print("\n=== Program Kalkulasi IPK ===")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Daftar Mahasiswa")
    print("3. Keluar")

    choice = input("Pilih opsi (1/2/3): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        print("\nTerima kasih! Sampai jumpa.")
        break
    else:
        print("Opsi tidak valid. Silakan pilih kembali.")
