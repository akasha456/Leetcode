
    """
    Bubble Sort - O(n²)
    Repeatedly swaps adjacent elements if they are in the wrong order.
    """

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap elements
                
    return arr

# Example usage
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = bubble_sort(numbers)
print("Sorted Array:", sorted_numbers)
