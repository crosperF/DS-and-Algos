def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        smallest_idx = i
        for j in range(i, n):
            if arr[smallest_idx] > arr[j]:
                smallest_idx = j

        arr[smallest_idx], arr[i] = arr[i], arr[smallest_idx]

    return arr


# Test Case 1: Basic Unsorted Array
arr1 = [64, 34, 25, 12, 22, 11, 90]
print("Test Case 1:", selection_sort(arr1))

# Edge Case 1: Already Sorted Array
arr2 = [1, 2, 3, 4, 5]
print("Edge Case 1:", selection_sort(arr2))  # Expected Output: [1, 2, 3, 4, 5]

# Edge Case 2: Array with All Identical Elements
arr3 = [5, 5, 5, 5]
print("Edge Case 2:", selection_sort(arr3))  # Expected Output: [5, 5, 5, 5]

# Edge Case 3: Empty Array
arr4 = []
print("Edge Case 3:", selection_sort(arr4))  # Expected Output: []

# Edge Case 4: Array with One Element
arr5 = [10]
print("Edge Case 4:", selection_sort(arr5))  # Expected Output: [10]

# 100 20 13 41 90
#  13 20  41  90 100
