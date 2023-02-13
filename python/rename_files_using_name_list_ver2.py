import os
import re

# get the list of texts from file XY
text_file = open("chapters.txt", "r", encoding="utf-8")
text_list = text_file.readlines()
text_list = [x.strip() for x in text_list if x.startswith(tuple(str(i).zfill(2) for i in range(1, 100)))] # only keep lines starting with two digits number
text_dict = dict(zip(text_list, text_list)) # create a dictionary from the list of texts

print('\n text_list \n') 
print(text_list)

print('\n text_dict \n') 
print(text_dict)

# go through files in the current folder
for filename in os.listdir(os.getcwd()):
    if not filename.endswith(".pdf"):
        continue # only process .pdf files
    file_number = re.findall(r"\b\d{1,2}", filename)[-1] # use regular expression to extract the last 1 or 2 digits in the file name
    file_number = file_number.zfill(2) # pad the extracted string to 2 digits
    print('*** '+ filename +' ... '+ file_number +'\n')
    if file_number in text_dict:
        new_filename = text_dict[file_number] + ".pdf" # create a new file name using the paired text
        print('+++ '+ new_filename)
        os.rename(filename, new_filename)
