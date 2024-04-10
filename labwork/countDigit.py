def count_digit(string):
    count = 0

    for ch in string:
        if ch.isdigit():
            count += 1
    return count


string = input("Enter a string :")
print(count_digit(string))