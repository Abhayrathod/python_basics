'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
#---------------------------------------------

# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]

# abhay = Solution()
# sum = abhay.twoSum([2,7,9,11,13],9)
# print(sum)

#---------------------------------------------
from typing import List

nums = [2,7,11,15]
target = 9

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         values = {}
#         for idx, value in enumerate(nums):
#             if target - value in values:
#                 return [values[target - value], idx]
#             else:
#                 values[value] = idx



#---------------------------------------Alternate solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]] 


#-------------------------run below

abhay = Solution()
a = abhay.twoSum(nums, target)
print(a)


