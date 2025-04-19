class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, last_element = 0, len(nums)
        while i < last_element:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                last_element -= 1
            else:
                i += 1