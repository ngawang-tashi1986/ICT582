l, h = 23, 578 # initializing l and h
odd, even = 0, 0 # initializing odd and even
 
# for loop to check for odd and even numbers
for i in range(l, h+1):
    if i % 2: # checking for odd numbers
        odd += 1 # increase odd count
    else:
        even += 1 # increase even count
 
# printing the output
print("Odd count is :", odd)
print("Even count is :", even)