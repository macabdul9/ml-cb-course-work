import math
def isPrime(N):
    if N < 2:
        return False
    if N == 2 or N == 3:
        return True

    for i in range(2, math.ceil(math.sqrt(N)), 1):
        if N%i == 0:
            return False
    return True

if __name__ == '__main__':
    N = int(input())
    if isPrime(N):
        print("Prime")
    else:
        print("Not Prime")