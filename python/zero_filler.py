start = 1
end = 3060
x = 1

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

print('\n\n*** result = ' + numStr(x) +'\n\n')