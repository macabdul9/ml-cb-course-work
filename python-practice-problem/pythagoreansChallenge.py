import math
if __name__ == '__main__':
    N = int(input())
    while N:
        A = int(input())
        N -= 1

        sq = math.ceil(math.sqrt(A))

        for i in range(sq + 1):
            for j in range(i, sq + 1, 1):
                sum = i*i + j*j
                if sum == A:
                    print("(",i,",",j,")", sep= "", end= " ")
        print()
