# Program for data unit conversion (KB, MB, GB)
print("Program data unit conversion")
print("=" * 10)
print("1. Kilobyte(KB)")
print("2. Megabyte(MB)")
print("3. Gigabyte(GB)", end="\n\n")

value = float(input("Input value to convert : "))
init_data = input("Initial data unit (1/2/3) : ")
des_data = input("Destination data unit (1/2/3) : ")

if value < 0:
    print("value cannot be smaller than 0")
else:
    if init_data == "1" and des_data == "2":
        result = value / 1_000
        print(f"Result from {value:,} KB is {result:,} MB")
    elif init_data == "1" and des_data == "3":
        result = value / 1_000_000
        print(f"Result from {value:,} KB is {result:,} GB")
    elif init_data == "2" and des_data == "1":
        result = value * 1_000
        print(f"Result from {value:,} MB is {result:,} KB")
    elif init_data == "2" and des_data == "3":
        result = value / 1_000
        print(f"Result from {value:,} MB is {result:,} GB")
    elif init_data == "3" and des_data == "1":
        result = value * 1_000_000
        print(f"Result from {value:,} GB is {result:,} KB")
    elif init_data == "3" and des_data == "2":
        result = value * 1_000
        print(f"Result from {value:,} GB is {result:,} MB")
    else:
        print("- Enter Options 1-4 only")
        print("- The initial of the data cannot be the same as the destination data")
