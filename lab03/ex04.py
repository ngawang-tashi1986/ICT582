numebrs = "123456789"

# Outer loop for each row
for i in range(len(numebrs), 0, -1):  # Decrement to print in reverse
    for j in range(i):  # Inner loop for printing each digit in a row
        print(numebrs[j], end='')  # Print digit with no newline
    print()  # Newline after completing each row