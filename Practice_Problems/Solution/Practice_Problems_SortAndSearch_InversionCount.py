def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Recursively split the halves
        inversions = mergeSort(L) + mergeSort(R)

        # Merging the two halves
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                inversions += (mid - i)  # Counting inversions
            k += 1

        # Checking for any leftover elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        return inversions
    else:
        return 0


# Test the function with an array
arr = [2, 1, 3, 1, 2]
inversion_count = mergeSort(arr)
print("Number of inversions:", inversion_count)  # Expected output: 4