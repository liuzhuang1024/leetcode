def partition(left, right, arr):
    if left > right:
        return 
    p = arr[left]
    min_left = []
    max_right = []
    for i in range(left, right):
        if p < arr[i]:
            max_right.append(arr[i])
        else:
            min_left.append(arr[i])
    arr[left:right] = min_left + max_right
    if k>len(min_left):
        partition(left, len(min_left)-1, arr)
    elif k<len(min_left):
        partition(len(min_left)+1, right, arr)
    else:
        return arr[:k]
if __name__ == "__main__":
    arr = [1,2,34,5,5,33,433,42,1,4,5,6]
    k = 5
    print(partition(0, len(arr)-1, arr))
