
# O(n ^ 2) Algorithm to sort an array

def bubble_sort(arr):
    for i in range(len(arr) - 1, -1, -1):
        swaped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swaped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swaped:
            break
    return arr


# Test Case 1: Basic Unsorted Array
arr1 = [64, 34, 25, 12, 22, 11, 90]
print("Test Case 1:", bubble_sort(arr1))  # Expected Output: [11, 12, 22, 25, 34, 64, 90]

# Edge Case 1: Already Sorted Array
arr2 = [1, 2, 3, 4, 5]
print("Edge Case 1:", bubble_sort(arr2))  # Expected Output: [1, 2, 3, 4, 5]

# Edge Case 2: Array with All Identical Elements
arr3 = [5, 5, 5, 5]
print("Edge Case 2:", bubble_sort(arr3))  # Expected Output: [5, 5, 5, 5]

# Edge Case 3: Empty Array
arr4 = []
print("Edge Case 3:", bubble_sort(arr4))  # Expected Output: []

# Edge Case 4: Array with One Element
arr5 = [10]
print("Edge Case 4:", bubble_sort(arr5))  # Expected Output: [10]

# 100 20 13 41 90
#  13 20  41  90 100
