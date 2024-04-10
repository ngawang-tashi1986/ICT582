def capitalize_list(list_of_words):

  for i in range(len(list_of_words)):
    list_of_words[i] = list_of_words[i].upper()

# Create a list of words
L = ["python", "is", "a", "programming", "language"]

# Capitalize the words in the list (modifying the original list)
capitalize_list(L)

# Print the capitalized words
print(L)
