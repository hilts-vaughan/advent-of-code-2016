def sequence_to_histogram(seq):
  o = {}
  for s in seq:
    if s in o:
      o[s] = o[s] + 1
    else:
      o[s] = 1
  return o

def shifttext(text, shift):
    a = ord('a')
    return ''.join(
        chr((ord(char) - a + shift) % 26 + a) if 'a' <= char <= 'z' else char
        for char in text.lower())

def get_next_biggest_from_histogram(histo):
  largest = 1111
  keys = []
  for key, val in histo.items():
    if val < largest:
      keys = [key]
      largest = val
    elif val is largest:
      keys.append(key)
  keys.sort(key=str.lower)
  a = keys[0]
  del histo[a]
  return a

rows = []
with open('input') as inputfile:
    rows = [line.split() for line in inputfile]
rows = rows[0:len(rows)]
print(rows)

soln = ""
for colId in range(0, 8):
    print(colId)

    cols = []
    for row in rows:
        c = row[0][colId]
        cols.append(c)
    c = "".join(cols)
    print(c)

    h = sequence_to_histogram(c)
    print(h)
    x = get_next_biggest_from_histogram(h)
    soln = soln + x
    print(soln)
print(soln)
