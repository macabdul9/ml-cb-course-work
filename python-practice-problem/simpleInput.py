if __name__ == '__main__':
    sum = 0
    while True:
        n = int(input())
        sum += n
        if sum < 0:
            break
        print(n)