#Python program to reverse the given string and compare it with the build in function

# s takes in the user input string to reverse
s = input("Enter any string : ")
reverse_s = ""  # Initally assigning the reserved string to null 

for i in range(len(s)):          # Calculate the length of string and traverse through string
    reverse_s += s[len(s) -1 -i] # Save the value of s[len(s) -1] to reverse_s with decrement index 

print("The Reversed string is : ", reverse_s)

# Calling build in reverse function, [::-1] means start at the end of string and end at position 0
# and move with the step -1, which means one step backwards.
build_in_reverse_s = s[::-1] 

print("Reversed String using build in function is : ", build_in_reverse_s)

if reverse_s == build_in_reverse_s:  # Comparing build in reverse function with looped reversed string
    print("The two reversed string are same")
else:
    print("The two reversed string are not same")
    