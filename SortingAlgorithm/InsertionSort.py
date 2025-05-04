
"""
Insertion Sort - O(n²) in worst case, O(n) in best case (already sorted).
Builds a sorted list by inserting each element in its correct position.
"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift larger elements to the right
            j -= 1
        
        arr[j + 1] = key  # Insert key at correct position

    return arr

# Example usage
numbers = [12, 11, 13, 5, 6]
sorted_numbers = insertion_sort(numbers)
print("Sorted Array:", sorted_numbers)
