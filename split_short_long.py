import os, shutil, glob

data_length_limit = 1000
data_dir = os.path.join('data', 'full-qn')
data_dir_short = os.path.join('data', 'short')
data_dir_long = os.path.join('data', 'long')
count_data_short = 0
count_data_long = 0


def prepare_output_dirs(dir):
    # empty content of long dir if exists
    if os.path.exists(dir):
        for filename in os.listdir(dir):
            os.remove(os.path.join(dir, filename))
    # make dir if don't already exist
    else:
        os.makedirs(dir)

prepare_output_dirs(data_dir_short)
prepare_output_dirs(data_dir_long)


# Loop through all file names in data directory
for filename in os.listdir(data_dir):
    # We're only interested in .txt files
    if filename.endswith(".txt"):
        filepath = os.path.join(data_dir, filename)

        # Read in content from file
        with open(filepath, 'r') as f:
            # Assign text content from file as a string variable
            data = f.read()
            # Split string into list of words (removing unwanted characters)
            data_words = data.replace("\n", " ").split(" ")
            # Clean the list, removing empty items
            data_words_clean = list(filter(("").__ne__, data_words))
            # Data lengths
            data_words_length = len(data_words_clean)
            data_length = len(data)
            # Copy current file into short if < data_length_limit, otherwise copy to long
            # print(filepath + ": " + str(data_length))
            if data_length < data_length_limit:
                shutil.copy(filepath, data_dir_short)
                count_data_short += 1
            else:
                shutil.copy(filepath, data_dir_long)
                count_data_long += 1

print("Short file count: " + str(count_data_short))
print("Long file count: " + str(count_data_long))
