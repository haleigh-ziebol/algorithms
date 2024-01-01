def interpolation_search(arr, x):
 low = 0
 high = len(arr) - 1 ## last element in array

 while low <= high and x >= arr[low] and x <= arr[high]:
    if low == high:
        if arr[low] == x:
            return low
        return -1
 
    pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))

    if arr[pos] == x:
        return pos

    if arr[pos] < x:
        low = pos + 1 ## too low
    else:
        high = pos - 1 ## too high

 return -1


# Example usage
arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
x = 18
index = interpolation_search(arr, x)

print("Element found at index", index) if index != -1 else print("Element not found")


