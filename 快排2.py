# def quick_sort(array, left, right):
#     if left < right:
#         q = partition(array, left, right)
#         quick_sort(array, left, q - 1)
#         quick_sort(array, q + 1, right)


def partition(array, left, right):
    if left >= right:
        return
    key = array[left]
    low = left
    high = right
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    print(array)
    partition(array, low, left - 1)
    partition(array, left + 1, high)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 56, 7, 4, 56666, 43, 1, 2, 3, 45, 322, 445, 6]
    partition(arr, 0, len(arr) - 1)
    print(arr)

