def solve(arr: list) -> int:
    if not arr:
        return 
    dic = {}
    if len(set(arr)) == len(arr):
        return arr[0]
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
            return i
if __name__ == "__main__":
    arr = [2, 3, 1, 0, 2, 5, 3]
    res = solve(arr)
    print(res)