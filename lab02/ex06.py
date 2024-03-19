sum_of_even_numbers = 0
for i in range(24, 579):
    if i % 2 == 0:
        sum_of_even_numbers += i
print(f"The sum of all even numbers between 23 and 578 is {sum_of_even_numbers}.")