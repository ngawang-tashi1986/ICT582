s = input("Enter any string : ")
reverse_s = ""

for i in range(len(s)):
    reverse_s += s[len(s) -1 -i]

print("The Reversed string is : ", reverse_s)

build_in_reverse_s = s[::-1]

print("Reversed String using build in function is : ", build_in_reverse_s)

if reverse_s == build_in_reverse_s:
    print("The two reversed string are same")
else:
    print("The two reversed string are not same")
    