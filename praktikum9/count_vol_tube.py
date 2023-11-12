# Program untuk menghitung volume tabung


def tube_volume(radius=7, height=10):
    """
    Mengembalikan hasil hitung volume tabung

    radius(float) : jari jari tabung (default : 7)
    height(float) : tinggi tabung (default : 10)
    """

    PI = 3.14
    return PI * (radius**2) * height


rad = float(input("Masukkan jari jari tabung : "))
hgt = float(input("Masukkan tinggi tabung : "))

volume = tube_volume(rad, hgt)

print(f"Volume tabung dengan jari-jari {rad} dan tinggi {hgt} adalah {volume:.2f}")
