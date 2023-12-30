def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

example_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(example_list)
print(sorted_list)