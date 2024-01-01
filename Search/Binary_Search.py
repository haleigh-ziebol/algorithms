def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right: ## search continues only with valid search space
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
print("Index of 7:", binary_search(sorted_array, 7))
print("Index of 8:", binary_search(sorted_array, 8))
print("Index of 1:", binary_search(sorted_array, 1))
print("Index of 21:", binary_search(sorted_array, 21))



