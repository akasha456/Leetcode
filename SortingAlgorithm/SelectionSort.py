"""
    Selection Sort - O(n²)
    Finds the smallest element and moves it to the correct position in each pass.
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:  # Find the minimum element
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap

    return arr

# Example usage
numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print("Sorted Array:", sorted_numbers)
