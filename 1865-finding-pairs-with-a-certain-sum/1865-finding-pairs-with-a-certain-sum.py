class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.val2ToCount = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        val2ToUpdate = self.nums2[index]
        val2UpdatedVal = val2ToUpdate + val
        self.val2ToCount[val2ToUpdate] -= 1
        self.val2ToCount[val2UpdatedVal] += 1
        self.nums2[index] = val2UpdatedVal

    def count(self, tot: int) -> int:
        ans = 0
        for val1 in self.nums1:
            val2Target = tot - val1
            ans += self.val2ToCount[val2Target]
        
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)