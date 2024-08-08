# Find Closest Number to Zero

from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # To start the closest number is the first item in the array
        closest = nums[0]
        # Loop through the array and if the abs of the looped number is less than the abs of the currest closest, define that as the closest
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        
        # If the number is a negative number and it is in the array
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        # If the number is a positive number
        else:
            return closest