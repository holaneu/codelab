# verze upravena ChatGPT:
# To make the code more secure and less prone to errors, I used try and except blocks to catch any potential exceptions that may occur when creating directories or opening files. 
# It also uses os.path.join() instead of concatenating strings to create file pathss, as this is a more robust way of handling file paths across different operating systems.

import os
import re

folder = '/content/sample_data/files/'

# first preparing testing data - create folder, create files
titles = '1 title1, 03 title3, 11 title11, 2 title2, 10 title10'
new_files = 'filename2, filename3, filename10, filename11'.split(', ')
os.makedirs(folder, exist_ok=True)
try:
  with open(os.path.join(folder, 'titles.txt'), 'w', encoding="utf-8") as rf:
    rf.write(titles.replace(', ', '\n'))
except Exception as e:
  print(f"Error while writing to file: {e}")

for fname in new_files:
  try:
    with open(os.path.join(folder, fname + '.txt'), 'w', encoding="utf-8") as wf:
      wf.write('Lorem ipsum')
  except Exception as e:
    print(f"Error while writing to file: {e}")

# Now I can use prepared testing data:
# Get the list of all files in folder and load file containing list of titles:
files = os.listdir(folder)
try:
  with open(os.path.join(folder, 'titles.txt'), "r", encoding="utf-8") as rf:
    textfile = rf.read().splitlines()
except Exception as e:
  print(f"Error while reading file: {e}")

print('*** files: ', files)
print('*** textfile lines: ', textfile)

titles_lookup = {}

for item in textfile:
  pattern = '(^\d{1,})( ?.+$)'
  parsed = re.match(pattern, item)
  if parsed:
    t_num = parsed.groups()[0].zfill(2)
    t_text = parsed.groups()[1].strip()
    titles_lookup[t_num] = f"{t_num} - {t_text}"

print(f'titles_lookup: {titles_lookup}\n')

for f in files:
  if '.txt' not in f:
    continue  # only process .txt files
  f_name, f_ext = os.path.splitext(f)
  pattern = '(^\D+)(\d{1,}$)'
  fn_parsed = re.match(pattern, f_name)
  if fn_parsed:
    f_title = fn_parsed.groups()[0]
    f_num = fn_parsed.groups()[1].zfill(2)
    if titles_lookup.get(f_num):
      new_name = str(titles_lookup.get(f_num) + f_ext)
      print(f, new_name)
      try:
        os.rename(os.path.join(folder, f), os.path.join(folder, new_name))
      except Exception as e:
        print(f"Error while renaming file: {e}")
