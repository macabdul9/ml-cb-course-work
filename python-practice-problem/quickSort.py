import random
def utility(arr, start, end):
    if start >= end:
        return


    pivot = arr[end]
    i = start - 1
    for j in range(start, end, 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    utility(arr, start, i)
    utility(arr, i + 2, end)


def quick_sort(arr):
    size = len(arr)
    utility(arr, 0, size - 1)


if __name__ == '__main__':
    N = int(input())
    arr = []
    arr = list(map(int, input().split()))
    quick_sort(arr)
    for i in range(N):
        print(arr[i], end= " ")
    print()
    arr.clear()
