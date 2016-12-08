def get_abbas(word):
    abbas = []
    for i in range(0, len(word) - 3):
        f = word[i]
        inner_one = word[i+1]
        inner_two = word[i+2]
        l = word[i+3]

        if (f is l) and (inner_two is inner_one) and (inner_one is not f) and (inner_one is not l):
            abbas.append(f + inner_one + inner_two + l)
    return abbas

def get_bab(word, invert):
    babs = []
    for i in range(0, len(word) - 2):
        f = word[i]
        m = word[i+1]
        l = word[i+2]

        if f is l and (m is not f):
            if not invert:
                babs.append(f + m + l)
            else:
                if (m + f + m) is not (f + m  + l):
                    babs.append(m + f + m)

    return babs

def supports_ssl(word):
    hyper_abbas = []
    word_abbas = []

    while True:
        hyper_start = word.find('[')
        hyper_end = word.find(']')

        if hyper_start > -1 and hyper_end > 1:
            # Get part without hyper
            hyper_text = word[hyper_start+1:hyper_end]
            hyper_abbas = hyper_abbas + get_bab(hyper_text, True)
            word = word[0:hyper_start] + "|" + word[hyper_end + 1:len(word)]
        else:
            break


    word_abbas = get_bab(word, False)
    for x in word_abbas:
        if x in hyper_abbas:
            return True
    return False

def supports_tls(word):
    hyper_abbas = []
    word_abbas = []

    while True:
        hyper_start = word.find('[')
        hyper_end = word.find(']')

        if hyper_start > -1 and hyper_end > 1:
            # Get part without hyper
            hyper_text = word[hyper_start+1:hyper_end]
            hyper_abbas = hyper_abbas + get_abbas(hyper_text)
            word = word[0:hyper_start] + "|" + word[hyper_end + 1:len(word)]
        else:
            break


    word_abbas = get_abbas(word)
    print(word_abbas)
    print(hyper_abbas)

    return len(word_abbas) > 0 and len(hyper_abbas) is 0

successes = 0
for line in open('input'):
    line = line.rstrip('\n')
    # print(line)
    if supports_ssl(line):
        successes = successes + 1

print(successes)
