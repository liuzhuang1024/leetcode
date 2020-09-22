# def partition(arr, left, right):
import random
arr = list(range(1, 14))
arr += list(range(5, 16))

print(arr)
random.shuffle(arr)
print(arr)
left = 0
right = len(arr) - 1  
index = left
key = arr[index]
left += 1
print(key)


def partition(arr, left, right):
    while left < right:
        while left < right and arr[right] >= key:
            right -= 1
        while left < right and arr[left] < key:
            left += 1
        arr[right], arr[left] = arr[left], arr[right]
        print(arr, left, right)
    arr[index], arr[left] = arr[left], arr[index]
    print(arr)
    return right
if __name__ == "__main__":
    import random
    arr = list(range(1, 14))
    arr += list(range(5,16))
    print(arr)
    random.shuffle(arr)
    print(arr)
    partition(arr, 0, len(arr)-1)
