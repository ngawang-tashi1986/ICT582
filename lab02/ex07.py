#Prompt user to enter start and end number
start_no = int(input("Enter first number : ")) 
end_no = int(input("Enter second number : "))
sum_of_even_numbers = 0 #initialize the sum of all even to zero 

# check if starting numebr is less than ending number
if start_no > end_no:
    print("Second number cannot be smaller then first number")
else:
    # use for loop to iterate through the range
    for i in range(start_no, end_no + 1): # end_no + 1 because range() is exclusive of last no
        if i % 2 == 0:  #check if the number is even
            sum_of_even_numbers += i # add the current even to the last sum
    #used string formate to display the output message            
    print(f"The sum of all even numbers between {start_no} and {end_no} is {sum_of_even_numbers}.")
