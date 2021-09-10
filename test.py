length_limit = 500
# Read in content from file
f = open("data/full-qn/QN35_1.txt", "r")
# Assign text content from file as a string variable
data = f.read()
# Split string into list of words (removing unwanted characters)
data_words = data.replace("\n", " ").replace(".", "").split(" ")
# Clean the list, removing empty items
data_words_clean = list(filter(("").__ne__, data_words))
# Data lengths
data_words_length = len(data_words_clean)
data_length = len(data)
# 
print(data_length)