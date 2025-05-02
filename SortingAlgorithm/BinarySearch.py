
    """
    Binary Search – O(log n)
    Efficiently finds the target in a sorted list by repeatedly dividing the search space.
    """


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Middle index
        if arr[mid] == target:
            return mid  # Target found, return index
        elif arr[mid] < target:
            left = mid + 1  # Move to right half
        else:
            right = mid - 1  # Move to left half
    
    return -1  # Target not found

# Example usage
numbers = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(numbers, target)
print("Element found at index:", result)
