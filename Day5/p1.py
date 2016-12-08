import hashlib

input = "abbhdwsy"


i = 0
p = ""
while len(p) < len(input):
    # Start
    i = i + 1
    m = hashlib.md5()
    m.update(input.encode('utf-8'))
    m.update(str(i).encode('utf-8'))
    hex = m.hexdigest()

    if hex.startswith("00000"):
        p = p + hex[5]
        print(p)

print(p)
