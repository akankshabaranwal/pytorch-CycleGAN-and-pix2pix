import random
import os

# Get a list of files
file_names = os.listdir()
#print(file_names)
#exit()

tmp_names = [str(i) + ".tmp" for i in range(len(file_names))]

# Renaming to arbitrary filenames to avoid replacing
for old, new in zip(file_names, tmp_names):
    os.replace(old, new) 

# Shuffle the file names
random.shuffle(file_names)

# Randomize
for old, new in zip(tmp_names, file_names):
    if(old!=new):
        os.replace(old, new)
        print(f'Replacing {old} with {new}')
    else:
        print('Skipped replacing')
