# 1
for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end="")
    elif ch.islower():
        print(ch.upper(), end="")
    else:
        print(ch, end="")

print("")

# 2
s1 = "Where are the snows of yesteryear?"
s2 = s1.split()
print(s2[-2])

# 3
the_list = ["Where", "are", "the", "snows?"]
s = "*".join(the_list)
print(s)

# 4
s = "It is either easy or impossible"
s = s.replace("easy", "hard").replace("im", "")
print(s)
