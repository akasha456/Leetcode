class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap ={}
        #hashmap has format {num:index}
        for index,num in enumerate(nums):
            if target - num in hashmap:
                return [index,hashmap[target-num]]
            hashmap[num] = index

'''
    Complexity Summary:
    Time Complexity: O(n) (single pass, constant-time lookups)
    Space Complexity: O(n) (hashmap storing at most n elements)
'''


''' This solution efficiently finds two numbers that sum to target using a hash map.
    It iterates through nums, checking if the complement (target - num) is already stored—if yes, it returns the indices;
    otherwise, it adds the current number to the hash map for future lookups.'''
'''
    If (target - num) is already in the hashmap, it means we've previously seen a number that, when added to num, equals target.
'''
