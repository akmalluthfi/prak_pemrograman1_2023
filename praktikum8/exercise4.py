str_1 = input("Masukkan string 1: ")
str_2 = input("Masukkan string 2: ")


is_anagram = True

if len(str_1) == len(str_2):
    for i in str_1:
        if i not in str_2:
            is_anagram = False
            break
else:
    is_anagram = False

print(f"{str_1} dan {str_2} {'' if is_anagram else 'bukan'} merupakan anagram")
