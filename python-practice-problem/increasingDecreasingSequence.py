def decreasing(seq, i):
    if seq[i] == seq[i - 1] - 1:
        return True
    else:
        return False

def increasing(seq, i):
    if seq[i] == seq[i - 1] + 1:
        return True
    else:
        return False




if __name__ == '__main__':

    n = int(input())
    seq = []
    for i in range(n):
        seq.append(int(input()))

    dec, inc = True, True

    valid = True
    i = 1
    while i < len(seq):

        if dec:
            dec = decreasing(seq, i)
        else:
            inc = increasing(seq, i)

        i += 1
        if not inc:
            valid = False
            break


    if valid:
        print("true")
    else:
        print("false")