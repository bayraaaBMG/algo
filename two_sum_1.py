class Solution:
    def twoSum(self, nums, target):
        num_to_index = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in num_to_index:
                return [num_to_index[difference], i]
            
            num_to_index[num] = i

solution = Solution()

nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))  

nums2 = [3, 2, 4]
target2 = 6
print(solution.twoSum(nums2, target2))

nums3 = [3, 3]
target3 = 6
print(solution.twoSum(nums3, target3)) 
