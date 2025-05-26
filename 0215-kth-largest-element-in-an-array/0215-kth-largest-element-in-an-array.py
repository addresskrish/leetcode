class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(nums, k):
            pivot = random.choice(nums)
            left, right, mid = [], [], []
            
            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)
            
            if len(left) >= k :
                return quickselect(left, k)
            if len(left) + len(mid) < k:
                return quickselect(right, k-len(left)-len(mid))
            return pivot
            
        return quickselect(nums, k)