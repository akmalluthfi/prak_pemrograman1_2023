print("Program untuk mengurutkan bilangan bulat sesuai dengan input user")

while True:
    mode = input("Pilih mode pengurutan (1:Asc / 2:Desc) : ")

    if mode == "1" or mode == "2":
        break

nums = []
while True:
    num = int(input("Masukkan bilagan bulat : "))

    len_nums = len(nums)

    if mode == "1":
        for i in range(len_nums):
            # asc
            if num <= nums[i]:
                nums.insert(i, num)
                break

        if len_nums == len(nums):
            nums.append(num)
    else:
        for i in range(len_nums):
            # desc
            if num >= nums[i]:
                nums.insert(i, num)
                break

        if len_nums == len(nums):
            nums.append(num)

    print(nums)

    next = input("Masih ada bilangan yang ingin dimasukkan (y/t) ? ")
    if next != "y":
        print(nums)
        break
