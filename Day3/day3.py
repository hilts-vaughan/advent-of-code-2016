import itertools

f = open('input', 'r')
count = 0
total = 0
for l in f:
    items = l.split(" ")
    items = list(filter(None, items))
    items = list(map(int, items))
    items.sort()

    a = items[0]
    b = items[1]
    c = items[2]

    if (a + b) > c:
        count = count + 1
print(count)
