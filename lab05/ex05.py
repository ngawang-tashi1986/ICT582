def capitalize_list(list_of_words):
  capitalized_list = []
  for word in list_of_words:
    capitalized_list.append(word.capitalize())
  return capitalized_list

# Create a list of words
L = ["python", "is", "a", "programming", "language"]

# Capitalize the words in the list
capitalized_words = capitalize_list(L)

# Print the capitalized words
print(L)
print("Capitalized word:", capitalized_words)



