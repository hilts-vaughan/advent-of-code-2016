import hashlib

input = "abbhdwsy"


i = 0
p = ['' for i in range(0, 8)]
found = 0

while p.count('') > 0:
    # Start
    i = i + 1
    m = hashlib.md5()
    m.update(input.encode('utf-8'))
    m.update(str(i).encode('utf-8'))
    hex = m.hexdigest()

    if hex.startswith("00000"):

        index = 9999
        if hex[5].isdigit():
            index = int(hex[5])

        if index < 8:
            new_chr = hex[6]
            print(hex)
            if p[index] is '':
                p[index] = new_chr
            print(p)

print("".join(p))
