
def merge_array(arr, start, mid, end):

    size_left = mid - start + 1
    size_right = end - mid
    left_array = [None]*size_left
    right_array  = [None]*size_right


    for i in range(size_left):
        left_array[i] = arr[start + i]
    for i in range(size_right):
        right_array[i] = arr[mid + 1 + i]

    i, j, k = 0, 0, start

    while i < size_left and j < size_right:
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i += 1
            k += 1
        else:
            arr[k] = right_array[j]
            j += 1
            k += 1

    while i < size_left:
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < size_right:
        arr[k] = right_array[j]
        j += 1
        k += 1


def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end)//2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge_array(arr, start, mid, end)
    else:
        return



if __name__ == '__main__':
    N = int(input())
    arr = []
    arr = list(map(int, input().split()))
    merge_sort(arr, 0, len(arr) - 1)
    for i in range(N):
        print(arr[i], end= " ")
    print()
    arr.clear()