'''
    Linear Search (Brute Force) – O(n)
    
    Scans each element in a list one by one until the target is found.
'''

def linear_search(arr, target):
    for index, num in enumerate(arr):
        if num == target:
            return index  # Return the index if found
    return -1  # Return -1 if target is not in the list

# Example usage
numbers = [3, 5, 2, 8, 6]
target = 8
result = linear_search(numbers, target)
print("Element found at index:", result)
