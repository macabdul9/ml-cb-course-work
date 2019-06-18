if __name__ == '__main__':
    n =int(input())
    loss = 0
    for i in range(n, 0, -1):

        for j in range(1, i + 1, 1):
            print(j, sep=" ", end=" ")

        for k in range(loss + n - i):
            print("*", sep=" ", end=" ")
        loss = n - i
        print()
