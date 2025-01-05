class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Brute force approch
        # ans = set()
        # nums.sort()
        # n = len(nums)
        # for i in range(n - 2) :
        #     for x in range(i + 1, n - 1) :
        #         for k in range(x + 1, n) :
        #             if nums[i] + nums[x] + nums[k] == 0 :
        #                 ans.add((nums[i], nums[x], nums[k]))
        # return list(ans)

        #Optimize approch
        ans = set()
        nums.sort()
        n = len(nums)
        for i in range(n - 2) :
            x = i + 1
            k = n - 1
            while x < k :
                temp = nums[i] + nums[x] + nums[k]
                if temp == 0 :
                    ans.add((nums[i], nums[x], nums[k]))
                    x += 1
                elif temp < 0 :
                    x += 1
                else :
                    k -= 1
        return list(ans)