def search_lowest(arr):
    lowest = arr[0]
    lowest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < lowest:
            lowest = arr[i]
            lowest_index = i
    return lowest_index

def sort_by_select(arr):
    new_arr = []
    for i in range(len(arr)):
        lowest = search_lowest(arr)
        new_arr.append(arr.pop(lowest))
    return new_arr

print(sort_by_select([5, 3, 6, 2, 10]))