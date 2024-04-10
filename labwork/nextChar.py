def next_char(ch):
    if ch.isalpha():
        print(ord(ch))
        new_ch = ord(ch) + 1
        print(ch(new_ch))
        print(ch)
    else:
        print("Is not a character")

in_char = input("Enter a character")
next_char(in_char)
print(next_char(in_char))