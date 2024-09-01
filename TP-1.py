# Two-Pointers-1

## Problem1 (https://leetcode.com/problems/sort-colors/)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == None or len(nums) == 0:
            return
        low = 0
        mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high = high - 1
            elif nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low = low + 1
                mid = mid + 1
            else:
                mid = mid + 1
# TC = O(n), Sc = O(1)

## Problem2 (https://leetcode.com/problems/3sum/)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == None or len(nums) == 0:
            return []
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            low = i+1
            high = len(nums)-1
            while low < high:
                triplet = nums[i] + nums[low] + nums[high]
                if triplet == 0:
                    result.append([nums[i], nums[low], nums[high]])
                    low  = low + 1
                    high = high - 1
                    while low < high and nums[low] == nums[low - 1]:
                        low  = low + 1
                    while low < high and nums[high] == nums[high + 1]:
                        high  = high - 1
                elif triplet < 0:
                    low = low + 1
                else:
                    high = high -1
        return result   
# TC = O(n^2), SC= O(1)

## Problem3 (https://leetcode.com/problems/container-with-most-water/)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if height == None or len(height) == 0:
            return 0
        maximum = 0
        left = 0
        right = len(height) - 1
        while left < right:
            maximum = max(maximum, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return maximum
#TC = O(n), SC = O(1)