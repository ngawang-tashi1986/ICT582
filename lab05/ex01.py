def count_unique_elements(input_list):
    unique_elements = []  # Temporary list to store unique elements
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return len(unique_elements)  # Return the count of unique elements

# Test the function with different lists
test_list_1 = [1, "cat", 2, "cat", 2.3, 2]
test_list_2 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9]
test_list_3 = ["apple", "banana", "cherry", "apple", "cherry"]

# Call the function with each test list and print the results
print(f"Number of unique elements in test_list_1: {count_unique_elements(test_list_1)}")  # Should return 4
print(f"Number of unique elements in test_list_2: {count_unique_elements(test_list_2)}")  # Should return 9
print(f"Number of unique elements in test_list_3: {count_unique_elements(test_list_3)}")  # Should return 3
