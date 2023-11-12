numbers = [
    [
        "###",
        "# #",
        "# #",
        "# #",
        "###",
    ],
    [
        " # ",
        " # ",
        " # ",
        " # ",
        " # ",
    ],
    [
        "###",
        "  #",
        "###",
        "#  ",
        "###",
    ],
    [
        "###",
        "  #",
        "###",
        "  #",
        "###",
    ],
    [
        "# #",
        "# #",
        "###",
        "  #",
        "  #",
    ],
    [
        "###",
        "#  ",
        "###",
        "  #",
        "###",
    ],
    [
        "###",
        "#  ",
        "###",
        "# #",
        "###",
    ],
    [
        "###",
        "  #",
        "  #",
        "  #",
        "  #",
    ],
    [
        "###",
        "# #",
        "###",
        "# #",
        "###",
    ],
    [
        "###",
        "# #",
        "###",
        "  #",
        "###",
    ],
]


def is_valid(number):
    for num in number:
        if num not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Anda hanya boleh memasukkan angka (0 ... 9)")
            return False

    return True


def display_number(number):
    for i in range(5):
        for num in number:
            print(numbers[int(num)][i], end="  ")

        print("")


while True:
    number = input("Masukkan digit angka yang akan dicetak ke layar: ")

    if not number.isnumeric():
        print("Anda hanya boleh memasukkan angka (0 ... 9)")
        continue

    # if not is_valid(number):
    #     continue

    display_number(number)
