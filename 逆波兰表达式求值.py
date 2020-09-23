def solve(arr: list) -> int:
    nums = []
    res = 0
    while arr:
        char = arr.pop(0)
        if char[-1] in "0123456789":
            nums.append(int(char))
        elif char == '+':
            nums.append(nums.pop() + nums.pop())
        elif char == '-':
            nums.append(nums.pop(-2) - nums.pop())
        elif char == r'/':
            nums.append(int(nums.pop(-2) / nums.pop()))
        elif char == '*':
            nums.append(nums.pop() * nums.pop())
    return nums.pop()

            


if __name__ == "__main__":
    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]
    res = solve(tokens)
    print(res)
