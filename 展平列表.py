def flatten(p_list):
    if p_list:
        return p_list.pop() + flatten(p_list)
    return []
if __name__ == "__main__":
    print(flatten([[1, 2, 3, 4], [1, 3, 4, 4], [1, 2, 4, 5, 5]]))
    
