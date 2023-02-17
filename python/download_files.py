import requests
import wget

start = 1
end = 18
basic_url = 'https://example.com/'
source_folder = 'folder'

def numStr(x):
  end_chars = len(str(end))
  x_chars = len(str(x))
  filler = ''
  if end_chars > x_chars:
    for i in range(0, end_chars - x_chars):
      filler = filler + '0'
    result = filler + str(x)
  else:
    result = str(x)
  return result

for x in range(start, end + 1):
  url = basic_url + source_folder + '/' + numStr(x) + '.png'
  storage = './downloads/' + source_folder + '/' + numStr(x) + '.png'
  #storage = './downloads/test/' + numStr(x) + '.png'
  print(url)
  print(storage)
  # code version 1, using wget:
  wget.download(url, storage)

"""
  # code version 2, using requests:
  # instead of wget.download(url, storage) use this:
  myfile = requests.get(url)
  with open(storage, "wb") as f:
    f.write(myfile.content)
"""
