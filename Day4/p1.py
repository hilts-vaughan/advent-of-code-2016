from itertools import groupby

f = open('input', 'r')

def sequence_to_histogram(seq):
  o = {}
  for s in seq:
    if s in o:
      o[s] = o[s] + 1
    else:
      o[s] = 1
  return o
def get_next_biggest_from_histogram(histo):
  largest = 0
  keys = []
  for key, val in histo.items():
    if val > largest:
      keys = [key]
      largest = val
    elif val is largest:
      keys.append(key)
  keys.sort(key=str.lower)
  a =  keys[0]
  del histo[a]
  return a

# Returns Sector ID or None if it's not valid
def is_valid_room(s):
    last_hyphen = s.rfind('-')
    start_square = s.index('[')
    sector_id = int(s[last_hyphen+1:start_square])
    checksum =  s[start_square+1:len(s)-2]
    letters = s[0:last_hyphen].replace('-', '')

    histo = sequence_to_histogram(letters)

    for l in checksum:
      next_char = get_next_biggest_from_histogram(histo)
      if l is not next_char:
        return None
    return sector_id

sectors = []
for l in f:
    res = is_valid_room(l)
    if res is not None:
      sectors.append(res)
sum = sum(sectors)
print(sum)
